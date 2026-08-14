# Sources — MTD for Income Tax 2026/27 (toolkit test)

All URLs accessed 14 Aug 2026.

1. **GOV.UK — Find out if and when you need to use Making Tax Digital for
   Income Tax**
   https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax
   — thresholds (£50k/£30k/£20k) and start dates (Apr 2026/27/28); extracted
   clean text with trafilatura (7,232 chars).

2. **GOV.UK — Use Making Tax Digital for Income Tax (Introduction)**
   https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/introduction
   — quarterly update deadlines table; extracted with trafilatura (7,968
   chars).

3. **HMRC — MTD for Income Tax business population statistics (commentary)**
   https://www.gov.uk/government/statistics/making-tax-digital-for-income-tax-business-population-statistics
   — 7.0m ITSA individuals, ~2.9m (42%) above £20k; wave counts 864k/1,077k/975k.
   Statistical tables available as ODS only:
   https://assets.publishing.service.gov.uk/media/688b99f5fc784fa12a0890d1/Making_Tax_Digital_Statistics_Tables_2023_2024.ods

4. **HMRC — Income tax receipts: analysis by type (Table 2.8, PDF)**
   https://assets.publishing.service.gov.uk/media/5d67862bed915d53b6016322/Table_2.8_August_2019.pdf
   — Self Assessment net receipts series 2007-08 to 2018-19; parsed with
   pdfplumber (default cell extraction failed on merged cells; text strategy
   succeeded).

Also consulted (background, not cited in report):
- GOV.UK — Sign up for MTD for Income Tax
  https://www.gov.uk/guidance/sign-up-for-making-tax-digital-for-income-tax
- GOV.UK — Making Tax Digital for Income Tax collection
  https://www.gov.uk/government/collections/making-tax-digital-for-income-tax
- The Income Tax (Digital Obligations) Regulations 2026 (legislation.gov.uk)