import re
import json
import html
import random

def extract_lessons(text):
    lesson_pattern = re.compile(r'^(LESSON\s+\d+|Lesson\s+\d+)\s*$', re.MULTILINE)
    matches = list(lesson_pattern.finditer(text))
    lessons = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        lesson_text = text[start:end]
        lesson_name = m.group(1).strip()
        lessons.append((lesson_name, lesson_text))
    return lessons

def extract_questions(lesson_text):
    q_pattern = re.compile(r'^(\d+)\.\s*(?:\n)?\*\*Question:\*\*(.+?)(?=^\d+\.\s*(?:\n)?\*\*Question:\*\*|\Z)', re.MULTILINE | re.DOTALL)
    questions = []
    for m in q_pattern.finditer(lesson_text):
        q_num = int(m.group(1))
        q_body = m.group(2).strip()
        
        # Extract Answer(s)
        answer_match = re.search(r'\*\*Answer[s]?:\*\*(.+?)(?=\*\*Explanation|\*\*Explanation / Tip|\*\*Tip|\Z)', q_body, re.DOTALL)
        if not answer_match:
            answer_match = re.search(r'Answer[s]?:(.+?)(?=Explanation|\Z)', q_body, re.DOTALL)
        
        # Extract Explanation
        expl_match = re.search(r'\*\*Explanation[^*]*:\*\*(.+?)(?=\*\*Tip|\Z)', q_body, re.DOTALL)
        if not expl_match:
            expl_match = re.search(r'Explanation[^:]*:(.+?)(?=Tip|\Z)', q_body, re.DOTALL)
        
        q_text = q_body
        if answer_match:
            q_text = q_body[:answer_match.start()].strip()
        q_text = q_text.strip()
        
        answer_text = ""
        if answer_match:
            answer_text = answer_match.group(1).strip()
            answer_text = re.sub(r'\*\*', '', answer_text)
            answer_text = re.sub(r'\(1\)|\(2\)|\(3\)|\(4\)', '', answer_text)
            answer_text = answer_text.strip()
            # Remove trailing period if it's just punctuation
            answer_text = re.sub(r'\.\s*$', '', answer_text)
        
        explanation = ""
        if expl_match:
            explanation = expl_match.group(1).strip()
            explanation = re.sub(r'\*\*', '', explanation)
            explanation = explanation.strip()
        
        questions.append({
            'num': q_num,
            'question': q_text,
            'answer': answer_text,
            'explanation': explanation
        })
    return questions

def clean_text(t):
    t = t.replace('**', '').replace('*', '')
    t = html.escape(t, quote=False)
    return t

# ============ DISTRACTOR GENERATORS ============

YEARS = [1066, 1215, 1314, 1348, 1415, 1485, 1534, 1558, 1588, 1603, 1605, 1642, 1649, 1660, 1666, 1688, 1689, 1707, 1745, 1776, 1789, 1801, 1833, 1837, 1851, 1859, 1901, 1914, 1918, 1928, 1939, 1945, 1948, 1954, 1960, 1966, 1973, 1979, 1982, 1997, 2002, 2012, 2016]

PLACES_UK = ['England', 'Scotland', 'Wales', 'Northern Ireland', 'London', 'Cornwall', 'Wiltshire', 'Orkney', 'Suffolk', 'Yorkshire', 'Lancashire']
PLACES_NONUK = ['France', 'Spain', 'Germany', 'Italy', 'Ireland', 'Rome', 'Netherlands', 'America', 'Poland', 'Russia']

PEOPLE_HISTORY = ['Henry VIII', 'Elizabeth I', 'Charles I', 'Charles II', 'William the Conqueror', 'Oliver Cromwell', 'Bonnie Prince Charlie', 'Boudicca', 'King Alfred the Great', 'Robert the Bruce', 'William of Orange', 'King James II', 'Sir Robert Walpole', 'Winston Churchill', 'Margaret Thatcher', 'Clement Attlee', 'John Major', 'Tony Blair', 'Emmeline Pankhurst', 'Florence Nightingale', 'Mary Queen of Scots', 'Anne Boleyn', 'Sir Christopher Wren', 'Captain James Cook', 'Sir Isaac Newton', 'Francis Crick', 'Sir Tim Berners-Lee', 'Sir Edwin Lutyens', 'Sir Robert Watson-Watt', 'Arthur Conan Doyle', 'William Shakespeare', 'Geoffrey Chaucer', 'William Wordsworth', 'Charlie Chaplin', 'Edward Elgar', 'Nick Park', 'Clarice Cliff', 'Isambard Kingdom Brunel', 'Bobby Moore', 'Ellie Simmonds', 'Tanni Grey-Thompson']

MEDIA = ['Television', 'Radio', 'Newspapers', 'Internet', 'Social media']
CHURCHES = ['Church of England', 'Church of Scotland', 'Roman Catholic Church', 'Methodist Church', 'Baptist Church']
COURTS = ['Youth Court', 'Magistrates Court', 'Crown Court', 'High Court', 'Supreme Court', 'Justice of the Peace Court']

def generate_distractors(question, answer, lesson_num):
    q_lower = question.lower().strip()
    a_clean = answer.strip().rstrip('.')
    a_lower = a_clean.lower()
    
    distractors = []
    
    # --- True/False ---
    if 'true or false' in q_lower:
        if a_lower == 'true':
            distractors = ['False', 'Partially true', 'Cannot be determined']
        else:
            distractors = ['True', 'Partially false', 'Cannot be determined']
        return distractors[:3]
    
    # --- Year answers ---
    year_match = re.search(r'\b(1\d{3}|2\d{3})\b', a_clean)
    if year_match:
        year = int(year_match.group(1))
        others = [y for y in YEARS if abs(y - year) <= 60 and y != year]
        random.seed(year)
        random.shuffle(others)
        distractors = [f'In {y}' for y in others[:3]]
        if len(distractors) < 3:
            distractors += [f'In {year - 50}', f'In {year + 50}', f'In {year - 100}']
        return distractors[:3]
    
    # --- Age answers ---
    age_match = re.search(r'(\d+)\s*(year|years)', a_clean)
    if age_match:
        age = int(age_match.group(1))
        distractors = [f'{age - 3} years old', f'{age + 3} years old', f'{age + 7} years old']
        return distractors
    
    # --- Money/currency ---
    money_match = re.search(r'£(\d+)', a_clean)
    if money_match:
        amt = int(money_match.group(1))
        distractors = [f'£{amt - 1000}', f'£{amt + 1000}', f'£{amt * 2}']
        return distractors
    
    # --- Place answers ---
    for place in PLACES_UK:
        if place.lower() in a_lower:
            others = [p for p in PLACES_UK if p != place] + PLACES_NONUK
            random.seed(hash(place))
            random.shuffle(others)
            distractors = [f'In {o}' for o in others[:3]]
            return distractors
    
    # --- Person answers ---
    for person in PEOPLE_HISTORY:
        if person.lower() in a_lower:
            others = [p for p in PEOPLE_HISTORY if p != person]
            random.seed(hash(person))
            random.shuffle(others)
            return others[:3]
    
    # --- Media answers ---
    for med in MEDIA:
        if med.lower() in a_lower:
            others = [m for m in MEDIA if m != med]
            return others[:3]
    
    # --- Two-part answers (House of X and House of Y) ---
    house_match = re.search(r'(house of \w+) and (house of \w+)', a_lower)
    if house_match:
        h1, h2 = house_match.group(1), house_match.group(2)
        fake_houses = ['house of tudor', 'house of stuart', 'house of norman', 'house of plantagenet', 'house of windsor', 'house of hanover']
        others = [h for h in fake_houses if h not in (h1, h2)]
        random.seed(hash(a_clean))
        random.shuffle(others)
        return [f'{others[0].title()} and {others[1].title()}', f'{others[2].title()} and {others[0].title()}', f'{h1.title()} and {others[0].title()}'][:3]
    
    # --- "The X" answers ---
    the_match = re.match(r'^the\s+(.+)$', a_clean, re.IGNORECASE)
    if the_match:
        noun = the_match.group(1)
        distractors = [f'The {noun} Act', f'The {noun} Treaty', f'The {noun} Agreement']
        return distractors
    
    # --- Yes/No ---
    if a_lower in ('yes', 'no'):
        return ['Yes', 'No', 'Cannot be determined'] if a_lower == 'no' else ['No', 'Yes', 'Cannot be determined']
    
    # --- Number-only answers ---
    num_match = re.match(r'^\d+$', a_clean)
    if num_match:
        n = int(a_clean)
        distractors = [str(n - 5), str(n + 5), str(n * 2)]
        return distractors
    
    # --- Generic fallbacks based on question type ---
    if 'who' in q_lower[:20]:
        return ['A famous monarch', 'A religious leader', 'A military commander']
    if 'where' in q_lower[:20]:
        return ['In London', 'In Scotland', 'In Wales']
    if 'when' in q_lower[:20]:
        return ['In the Middle Ages', 'In the 18th century', 'In the 20th century']
    if 'what' in q_lower[:20]:
        return ['A type of law', 'A historical event', 'A royal decree']
    
    return ['None of the above', 'All of the above', 'Cannot be determined']

def lesson_to_code(lesson_name):
    m = re.search(r'(\d+)', lesson_name)
    return f'L{m.group(1)}' if m else 'L1'

def chapter_for_lesson(lesson_num):
    chapters = {
        1: 'The UK and citizenship', 2: 'Values and principles', 3: 'History - Early Britain',
        4: 'History - Tudors and Stuarts', 5: 'History - Georgian and Victorian',
        6: 'History - 20th Century Britain', 7: 'Government and law', 8: 'The role of Parliament',
        9: 'Rights and responsibilities', 10: 'British culture and traditions',
        11: 'UK in the world', 12: 'Citizenship and community', 13: 'Law and order',
        14: 'Public services and institutions', 15: 'Modern British society',
        16: 'UK economy and work', 17: 'Constitution and political system',
    }
    return chapters.get(lesson_num, 'British life and culture')

def main():
    with open('questions_source.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    
    lessons = extract_lessons(text)
    print(f'Found {len(lessons)} lessons')
    
    all_cards = []
    card_num = 1
    
    for lesson_name, lesson_text in lessons:
        lesson_code = lesson_to_code(lesson_name)
        lesson_num = int(re.search(r'(\d+)', lesson_name).group(1))
        chapter = chapter_for_lesson(lesson_num)
        questions = extract_questions(lesson_text)
        print(f'  {lesson_name} ({lesson_code}): {len(questions)} questions')
        
        for q in questions:
            distractors = generate_distractors(q['question'], q['answer'], lesson_num)
            options = [q['answer']] + distractors[:3]
            random.seed(card_num)
            random.shuffle(options)
            correct_index = options.index(q['answer'])
            
            card = {
                'n': card_num,
                'lesson': lesson_code,
                'chapter': chapter,
                'tf': False,
                'orig': clean_text(q['question']),
                'q': clean_text(q['question']),
                'ur': '',
                'opt': [clean_text(o) for o in options],
                'optur': ['', '', '', ''],
                'a': correct_index,
                'x': clean_text(q['explanation']) if q['explanation'] else clean_text(f'The correct answer is: {q["answer"]}'),
                'xur': ''
            }
            all_cards.append(card)
            card_num += 1
    
    print(f'\nTotal cards generated: {len(all_cards)}')
    
    # Validate
    bad_opt = [c for c in all_cards if len(c['opt']) != 4]
    bad_a = [c for c in all_cards if not (0 <= c['a'] <= 3)]
    missing_q = [c for c in all_cards if not c['q']]
    print(f'Cards without 4 options: {len(bad_opt)}')
    print(f'Cards with invalid answer index: {len(bad_a)}')
    print(f'Cards missing question: {len(missing_q)}')
    
    # Generate HTML
    html_template = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Life in the UK — 408 Multiple Choice Practice Questions</title>
<meta name="description" content="407 Life in the UK Test practice questions across 17 lessons, each with four multiple-choice options and one correct answer.">
<style>
:root{color-scheme:light dark;--bg:#f7f7f5;--surface:#ffffff;--ink:#171a20;--ink-2:#555c67;--ink-3:#878e99;--line:#e5e7ea;--line-2:#d4d8dd;--accent:#0f7a6b;--accent-ink:#0b5c51;--accent-soft:#e0ece8;--ok:#0f7a3d;--ok-soft:#e3f2e8;--bad:#a62a2a;--bad-soft:#fbe8e8;--warn:#b45309;--warn-soft:#fbeedd;--mono:IBM Plex Mono,ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;--sans:Geist,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;--display:Space Grotesk,var(--sans);--radius:14px;--shadow:0 1px 2px rgba(23,26,32,.05),0 8px 24px rgba(23,26,32,.06);--maxw:900px}
@media (prefers-color-scheme:dark){:root{--bg:#0f1216;--surface:#161a20;--ink:#e9ebee;--ink-2:#9aa3ae;--ink-3:#68717d;--line:#232930;--line-2:#313943;--accent:#3ec9b2;--accent-ink:#7fe3d2;--accent-soft:#14332c;--ok:#5fd08a;--ok-soft:#10291a;--bad:#f08a8a;--bad-soft:#2e141e}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:16.5px;line-height:1.72}
.container{max-width:var(--maxw);margin:0 auto;padding:24px}
h1{font-family:var(--display);font-size:30px;margin:0 0 4px}
.sub{color:var(--ink-2);font-size:14px}
.stats{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:16px;margin:24px 0;display:flex;gap:24px;flex-wrap:wrap}
.stat{flex:1;min-width:120px}
.stat .v{font-size:20px;font-weight:700;color:var(--accent-ink)}
.stat .l{font-size:13px;color:var(--ink-3)}
.card{border:1px solid var(--line);border-radius:var(--radius);background:var(--surface);padding:18px;margin:12px 0;position:relative}
.card .q-num{font-family:var(--mono);font-size:12px;color:var(--ink-3);position:absolute;top:14px;right:14px}
.card h3{font-family:var(--display);font-size:18px;margin:0 0 10px}
.card p.q{font-size:16px;font-weight:600;margin:0 0 10px}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.opt{padding:10px 12px;border:1px solid var(--line-2);border-radius:10px;background:var(--surface);cursor:pointer;text-align:left;font-size:14px}
.opt:hover{border-color:var(--accent-ink)}
.opt.correct{background:var(--ok-soft);border-color:var(--ok)}
.opt.incorrect{background:var(--bad-soft);border-color:var(--bad)}
.expl{margin-top:10px;padding-top:10px;border-top:1px solid var(--line);font-size:14px;color:var(--ink-2);display:none}
.expl b{color:var(--ink)}
.back{display:inline-block;margin-top:16px;padding:8px 16px;border:1px solid var(--line);border-radius:8px;text-decoration:none;color:var(--accent-ink)}
.back:hover{background:var(--accent-soft)}
footer{margin-top:32px;padding-top:24px;border-top:1px solid var(--line);font-size:13px;color:var(--ink-3)}
</style>
</head>
<body>
<div class="container">
<h1>Life in the UK — Multiple Choice Practice</h1>
<p class="sub">407 questions across 17 lessons · Each question has 4 options with 1 correct answer</p>

<div class="stats">
<div class="stat"><span class="v" id="totalCount">0</span><span class="l">Total Questions</span></div>
<div class="stat"><span class="v">17</span><span class="l">Lessons</span></div>
<div class="stat"><span class="v">4</span><span class="l">Options per Question</span></div>
</div>

<div id="lessonContainer"></div>

<script>
const CARDS = CARDS_DATA;
function esc(t){return t.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
function render(){
  const cont=document.getElementById("lessonContainer");
  const lessons=[...new Set(CARDS.map(c=>c.lesson))].sort();
  document.getElementById("totalCount").textContent=CARDS.length;
  lessons.forEach(le=>{
    const cards=CARDS.filter(c=>c.lesson===le);
    const chap=cards[0]?.chapter||"";
    const sec=document.createElement("section");
    sec.id=le;
    sec.innerHTML=`<h2 style="font-family:var(--display);margin:24px 0 8px">${le} · ${esc(chap)} <span style="font-size:14px;color:var(--ink-3);font-weight:normal">(${cards.length} questions)</span></h2><div class="cards" id="cards-${le}"></div>`;
    cont.appendChild(sec);
    const cardCont=document.getElementById(`cards-${le}`);
    cards.forEach(c=>{
      const div=document.createElement("div");
      div.className="card";
      div.innerHTML=`<span class="q-num">Q${c.n}</span><h3>${c.q}</h3><div class="opts">${c.opt.map((o,i)=>`<button class="opt" data-a="${i}">${["A","B","C","D"][i]}. ${o}</button>`).join("")}</div><div class="expl" id="expl-${c.n}"></div>`;
      cardCont.appendChild(div);
      div.querySelectorAll(".opt").forEach(b=>{
        b.addEventListener("click",()=>{
          const correct=c.a;
          div.querySelectorAll(".opt").forEach(x=>{
            x.disabled=true;
            if(+x.dataset.a===correct)x.classList.add("correct");
          });
          if(+b.dataset.a!==correct)b.classList.add("incorrect");
          const expl=document.getElementById(`expl-${c.n}`);
          expl.style.display="block";
          expl.innerHTML='<b>'+( +b.dataset.a===correct?"Sahi! Correct!":"Galat. Correct answer: "+esc(c.opt[c.a]))+'</b><br>'+esc(c.x);
        });
      });
    });
  });
}
render();
</script>
</body>
</html>
'''
    
    js_data = 'CARDS_DATA = ' + json.dumps(all_cards, ensure_ascii=False, indent=2)
    html_content = html_template.replace('CARDS_DATA', js_data)
    
    with open('life-in-uk-test-mcq.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f'Written life-in-uk-test-mcq.html with {len(all_cards)} cards')

if __name__ == '__main__':
    main()
