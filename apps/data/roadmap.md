# Road Map
Here there should be information about the next tools to develop

### V0.1 (Inside Testing)
- [x] ~~Deploy to Streamlit-Share (Issues accessing it in office laptops)~~
- [x] Deploy to Heroku app (Fixed issues, now accessible from any device)
    - [x] Sync with Github
    - [x] Automate Deployment
- [x] Multipage implementation (Hydralit)
    - [x] Menu on top
    - [x] Custom theme
- [x] Code refactoring
    - [x] Detach long text to separate markdown files
    - [x] Split data into DataFrame
    - [x] Parse external csv files into the app
- [x] Connect to Speckle
    - [x] Set speckle structure
        - [x] [case] **/** [study] **/** [metric] **/** [sub-metric1] 
            - rev1/daylight/DA/DA0to100 
            - rev1/daylight/DA/DAmt50 (LEED V4)
    - [x] Retreive and parse existing analysis for each project (specklepy)
        - [x] Branch name
- [ ] Complete analysis description
    - [ ] Solar Irradiation
    - [ ] Daylight
    - [ ] Outdoor Wind Comfort
    - [ ] Outdoor Thermal Comfort
    - [ ] Air Quality
- [x] Set simple Auth system (Streamlit) (difficult)
    - [x] Create user sign-in
    - [x] Create user log-in form
    - [x] Sample Logins
    - [x] Manage database in Database (Firebase, Google Sheet, Notion)
- [x] Incorporate custom text for each project/metric (easily done by the consultant)
    - [x] Speckle Globals, Google Sheets or Notion... 
        - [x] Send a Markdown formatted text to the project global
        - [x] Set project attributes -> Project name, client, etc
- [ ] Beta testing
    - [ ] User feedback

### V0.2 (launch beta)
- [ ] Document
  - [ ] Code
  - [ ] Tool usage in Notion
  - [ ] Development process in Notion ? 
- [ ] Read data from Speckle-> **Hard**
  - [ ] Decide on Tree Structure in GH 
  - [ ] Or read object directly with GraphAPI (ask in the forum is this is possible)
- [ ] Custom interactive visualizations
    - [ ] Each analysis requires different set of visuals? 
    - [ ] Common to all
        - [ ] Histogram
        - [ ] Bar chart
        - [ ] Pie chart
- [ ] Get properties from Speckle geometry
    - [ ] Face center point -> Height (eg. Used to separate analysis by floors )
### V0.3 ()
- [ ] Custom loader
- [ ] Custom domain deployment (hoarelea domain)
    - [ ] IT support to set-up

- [ ] Set Auth system Speckle (difficult)
    - [ ] Investigate