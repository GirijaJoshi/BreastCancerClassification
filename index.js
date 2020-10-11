// const myData = [
//
// 	  {word: 'Age', weight: 40},
// 	  {word: 'Race', weight: 39},
// 	  {word: 'Family History', weight: 11, color: 'green'},
// 	  {word: 'First Menarche Age', weight: 27},
// 	  {word: 'Age First Birth', weight: 36},
// 	  {word: 'BI-RADS Density', weight: 39},
// 	  {word: 'Hormone Therapy', weight: 12, color: 'green'},
// 	  {word: 'Menopause', weight: 27},
// 	  {word: 'BMI', weight: 36},
// 	  {word: 'Breast Biopsy', weight: 22},
// 	  text: "Breast Cancer History"{word: 'Breast Cancer History', weight: 40},
//   ]


// ZC.LICENSE = ["569d52cefae586f634c54f86dc99e6a9", "b55b025e438fa8a98e32482b5f768ff5"];
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
