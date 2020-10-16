

var myConfig = {
  type: 'wordcloud',
  options: {
    words: [
      {
        text: "Age",
        count: 13
      },
      {
        text: "Race",
          count: 1
      },
      {
        text: "Family History",
          count: 1
      },
      {
        text: "First Menarche Age",
          count: 1
      },
      {
        text: "Age First Birth",
          count: 3
      },
      {
        text: "BI-RAD Density",
          count: 6
      },
      {
        text: "Hormone Therapy",
          count: 5
      },
      {
        text: "Menopause",
          count: 1
      },
      {
        text: "BMI"
      },
      {
        text: "Breast Biopsy",
          count: 1
      },
      {
        text: "Breast Cancer History",
          count: 1
      }
    ],

    style: {
      borderRadius: 2,
      fontFamily: 'Scope One',
      padding: '5px 10px',
      hoverState: {
        alpha: 1,
        backgroundColor: 'white',
        borderColor: 0,
        fontColor: 'black',
        textAlpha: 1,
      },
      tooltip: {
        rules: [{ //Rule 1
          rule: '"%t" == "Age"',
          text: "fdsfdsfds",
          "font-weight": "bold",
          "background-color": "#ff9999"
        }]
      }
    }
  }
};

zingchart.render({
  id: 'myChart',
  data: myConfig,
  height: 400,
  width: '100%'
});
