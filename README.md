# NAS-2021-data
Ministry of Education's report dashboard available here: [https://nas.gov.in/report-card/nas-2021](https://nas.gov.in/report-card/nas-2021)

## Disclaimer 
The rights for the data belong to [DoSEL, MoE, GOI](https://www.education.gov.in/en/school-education) and [NCERT](https://ncert.nic.in/). I have only reorganised it. Don't @ me. Don't cite me.

The code files are released in the public domain. Feel free to do whatever you like with them.

## The data
The data here is organised into –
1. [**JSONs:**](./json_data/) These contain all the data from national, state and district reports, as downloaded from the dashboard. Might be a bit hard to parse.
2. [**CSVs:**](./csv_data/) These have been created out of the JSON data. Easier to read and use.

### Types of reports
1. **Highlights:** These contain demographic information such as land area, population and sex ratio.
  - State: [JSON](./json_data/NAS_highlights_state.json), [CSV](./csv_data/NAS_highlights_state.csv)
  - District: [JSON](./json_data/NAS_highlights_district.json), [CSV](./csv_data/NAS_highlights_district.csv)
2. **Participation:** These contain information about the schools, teachers and students who participated in NAS.
  - National: [JSON](./json_data/NAS_participation_national.json), [CSV](./csv_data/NAS_participation_national.csv)
  - State: [JSON](./json_data/NAS_participation_state.json), [CSV](./csv_data/NAS_participation_state.csv)
  - District: [JSON](./json_data/NAS_participation_district.json), [CSV](./csv_data/NAS_participation_district.csv)
3. **Performance:** These contain the subject-wise results. Data is available as percentage and scaled scores (at state level only), and is further disaggregated by gender, social group, location and school management.
  - State scaled score: [JSON](./json_data/NAS_performance_scaled.json), [CSV](./csv_data/performance_scaled_statewise/)
  - State percentage score: [JSON](./json_data/NAS_performance_percentage_state.json), [CSV](./csv_data/performance_percentage_statewise/)
  - District: [JSON](./json_data/NAS_performance_percentage_district.json), [CSV](./csv_data/performance_percentage_districtwise/)
4. **Learning outcomes:** These contain learning outcome-wise percentage performance.
  - State: [JSON](./json_data/NAS_learning_outcomes_state.json), [CSV](./csv_data/NAS_learning_outcomes_state.csv)
  - District: [JSON](./json_data/NAS_learning_outcomes_district.json), [CSV](./csv_data/NAS_learning_outcomes_district.csv)
5. **Feeback:** These contain responses to the questionnaire on learning during the pandemic.
  - National: [JSON](./json_data/NAS_feedback_national.json), [CSV](./csv_data/NAS_feedback_national.csv)
  - State: [JSON](./json_data/NAS_feedback_state.json), [CSV](./csv_data/NAS_feedback_state.csv)
  - District: [JSON](./json_data/NAS_feedback_district.json), [CSV](./csv_data/NAS_feedback_district.csv)

In addition, there are some helper files –
1. List of states/UTs with UDISE codes: [JSON](./json_data/NAS_state_udise_codes.json), [CSV](./csv_data/NAS_state_udise_codes.csv)
2. List of districts with UDISE codes: [JSON](./json_data/NAS_district_udise_codes.json), [CSV](./csv_data/NAS_district_udise_codes.csv)