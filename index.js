

var myConfig = {
  type: 'wordcloud',
  options: {
    words: [
      {
        text: "Age"
      },
      {
        text: "Race"
      },
      {
        text: "Family History"
      },
      {
        text: "First Menarche Age"
      },
      {
        text: "Age First Birth"
      },
      {
        text: "BI-RAD Density"
      },
      {
        text: "Hormone Therapy"
      },
      {
        text: "Menopause"
      },
      {
        text: "BMI"
      },
      {
        text: "Breast Biopsy"
      },
      {
        text: "Breast Cancer History"
      }
    ]
  }
};

zingchart.render({
  id: 'myChart',
  data: myConfig,
  height: 400,
  width: '100%'
});
