

var myConfig = {
  type: 'wordcloud',
  options: {
    words: [
      {
        text: "Age",
        count: 13,
        tooltip: {
          text: "Age is the largest risk factor for most types of cancer, including breast cancer.\n\
          The longer we live, the more opportunities there are for the human body to go through genetic mutations.\n\
          As we age, the body is less capable of repairing damaging mutations. 2 out of 3 invasive breast cancers \n\
          are found in women 55 and older. ",
          visible: true
        }
      },
      {
        text: "Race",
        count: 3,
        tooltip: {
          text: "- White women are more likley to develop breast cancer over the age of 45.\n\
          - Afriacn American women are more likely to develop breast cancer under the age of 45.\n\
          - African American women are more likely to die from breast cancer at any age.\n\
          - Asian, Hispanic, and Native American women have a lower risk of developing and dying from breast cancer. ",
          visible: true
        }
      },
      {
        text: "Family History",
        count: 1,
        tooltip: {
          text: "Around 15% of women with breast cancer have also had a family member with the disease.\n\
          Having a first-degree relative with breast cancer doubles a women's risk of being diagnosed.\n\
          Family history is important to look at because there are certain gene changes that can be inherited.\n\
          BRCA1 and BRCA2 are the two most common causes of hereditary breast cancer.\n\
          In normal cells, these genes help make proteins that repair damaged DNA.\n\
          Mutated vrsions of these genes can lead to abnormal cell groth, which can lead to cancer. ",
          visible: true
        }
      },
      {
        text: "First Menarche Age",
        count: 1,
        tooltip: {
          text: "There are ongoing study and researches to identify relationship, if any, exists between early\n\
          menarche with breast cancer.",
          visible: true
        }
      },
      {
        text: "Birth History",
          count: 3,
          tooltip: {
            text: "Women who have children before the age of 20 have a lower lifetime risk of breast cancer.\n\
            Mothers with five full-term pregnancies are about 50% less likely than nulliparous (women\n\
            who have not had children or breast fed) women to develop breast cancer.  Breastfeeding has\n\
            been found to reduce the risk of breast cancer.  This risk factor has to do with hormone \n\
            levels (as with menstruation, menopause, and HRT). The increased risk nulliparious women \n\
            have is do to the fact that they will have more ovulatory cycles and therefore menstruations \n\
            than women with biological children. ",
            visible: true
          }
      },
      {
        text: "BI-RAD Density",
          count: 6,
          tooltip: {
            text: "Breasts are made up of fatty tissue, fibrous tissue, and glandular tissue.\n\
            When women have more glandular and fibrous tissue, their breasts will appear more dense on a mammogram.\n\
            Women with more fatty tissue will appear to have less dense breasts on a mammogram.\n\
            Women with a higher breast density have 1.5-2x the likelihood of a positive breast cancer diagnosis.\n\
            Breast density is affected by most other risk factors, including age, menopausal status, hormonte \n\
            therapy, pregnancies, and genetics.",
            visible: true
          }
      },
      {
        text: "Hormone Therapy",
          count: 9,
          tooltip: {
            text: "There are two types of Hormone Replacement Therapy (HRT)\n\
            - Combination HRT: using the hormones estrogen and progesterone\n\
            - Estrogen-only HRT: using only estrogen\n\
            Both HRT methods increase the risk of breast cancer, but Combination HRT increases breast cancer risk\n\
            by 75% - even when used for a short time.  Combination HRT increases the likelihood that a diagnosis \n\
            will be found at a more advanced stage and also increases the likelihood that a woman will die from \n\
            breast cancer.",
            visible: true
          }
      },
      {
        text: "Menopause",
          count: 1,
          tooltip: {
            text: "The more menstrual cycles a woman incurs has a positive correlation for the likelihood of breast cancer.\n\
            Women who start menstruating early and start menopause later (usually after 55) are at higher risk,\n\
            mainly due to longer lifetime exposure to the hormones estrogen and progesterone.",
            visible: true
          }
      },
      {
        text: "BMI",
        count: 1,
        tooltip: {
          text: "Many studies have shown that, in postmenopausal women, a higher BMI is associated with a modest increase in risk of\n\
          breast cancer. For example, a 5-unit increase in BMI is associated with a 12% increase in risk. Among postmenopausal\n\
          women, those who are obese have a 20% to 40% increase in risk of developing breast cancer compared with normal-weight women.\n\
          The higher risks are seen mainly in women who have never used menopausal hormone therapy and for tumors that express hormone\n\
          receptors. Obesity is also a risk factor for breast cancer in men.\n\
          \n\
          In premenopausal women, by contrast, overweight and obesity have been found to be associated with a 20% decreased risk of\n\
          breast tumors that express hormone receptors ",
          visible: true
        }
      },
      {
        text: "Breast Biopsy",
        count: 1,
        tooltip: {
          text: "Women with earlier biopsies showing any of the following have a slight increased risk: fibroadenomas with complex features,\n\
          hyperplasia without atypia, sclerosing adenosis, and solitary papilloma.",
          visible: true
        }
      },
      {
        text: "Breast Cancer History",
        count: 1,
        tooltip: {
          text: "Around 15% of women with breast cancer have also had a family member with the disease.\n\
          Having a first-degree relative with breast cancer doubles a women's risk of being diagnosed.\n\
          Family history is important to look at because there are certain gene changes that can be inherited.\n\
          BRCA1 and BRCA2 are the two most common causes of hereditary breast cancer.\n\
          In normal cells, these genes help make proteins that repair damaged DNA.\n\
          Mutated vrsions of these genes can lead to abnormal cell groth, which can lead to cancer. ",
          visible: true
        }
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
