const lib = require("xlsx-populate");

const new_data = ["1", "2", "3", "4", "5", "6"];

const ALL_EXCEL_STYLES = [
  "bold",
  "italic",
  "underline",
  "strikethrough",
  "subscript",
  "superscript",
  "fontSize",
  "fontFamily",
  "fontGenericFamily",
  "fontScheme",
  "fontColor",
  "horizontalAlignment",
  "justifyLastLine",
  "indent",
  "verticalAlignment",
  "wrapText",
  "shrinkToFit",
  "textDirection",
  "textRotation",
  "angleTextCounterclockwise",
  "angleTextClockwise",
  "rotateTextUp",
  "rotateTextDown",
  "verticalText",
  "fill",
  "border",
  "borderColor",
  "borderStyle",
  "leftBorder",
  "rightBorder",
  "topBorder",
  "bottomBorder",
  "diagonalBorder",
  "leftBorderColor",
  "rightBorderColor",
  "topBorderColor",
  "bottomBorderColor",
  "diagonalBorderColor",
  "leftBorderStyle",
  "rightBorderStyle",
  "topBorderStyle",
  "bottomBorderStyle",
  "diagonalBorderDirection",
];

function normalXLSXPopulateTest(path) {
  lib.fromFileAsync(path).then((wb) => {
    const sheet = wb.sheet("Sheet1");

    const defaultWiDTH = 8.43;

    const totalColumn = 9;
    const totalRow = 11;
    const startAtRow = 1;
    const startAtColumn = 4;

    const newColumn1Index = 4;

    //get old file WIDTH
    let templateColumnWidth = [];
    for (let i = 1; i <= totalColumn; i++) {
      if (i === newColumn1Index) {
        const index = i == 1 ? 1 : i;
        templateColumnWidth.push(sheet.column(index).width());
      }
      templateColumnWidth.push(sheet.column(i).width());
    }

    console.log({ templateColumnWidth });

    let testData = sheet.usedRange().value();

    console.log({ testData });

    const newRangeFromRow = testData;

    testData.map((row, rowIndex) => {
      row.forEach((element, index) => {
        if (index === newColumn1Index) {
          newRangeFromRow[rowIndex].splice(index, 0, "Edited");
        }
      });
    });
    //theo docs cua xlsx populate thì chỉ cần lấy gốc đầu tiên của range để thay đổi giá trị cho toàn range theo format array row[[col,col,col],[col,col,col],....]
    sheet.cell("A1").value(newRangeFromRow);

    // //range luu theo row
    // //sheet range(number of row selected, number of columns selected, start at row, start at column)
    // const oldRangeFromCol = sheet
    //   .range(totalRow, totalColumn, startAtRow, startAtColumn)
    //   .value(); // lấy 11 row, 9 cột, bắt dầu từ row 1, băt đầu từ cột 4

    // const newRangeFromRow = oldRangeFromCol;

    // oldRangeFromCol.map((row, rowIndex) => {
    //   row.forEach((element, index) => {
    //     if (index === 0) {
    //       //index == 1 means that the head of the range i the index is 3 because the range is start at 4
    //       newRangeFromRow[rowIndex].splice(index, 0, "Edited");
    //     }
    //   });
    // });

    console.log({ newRangeFromRow });

    for (let i = 0; i <= totalColumn + 1; i++) {
      sheet.column(i + 1).width(templateColumnWidth[i]);
    }

    // sheet
    //   .range(totalRow, totalColumn + 1, startAtRow, startAtColumn)
    //   .value(newRangeFromRow);

    wb.toFileAsync("./output.xlsx");
  });
}

const pth = "./excel_test_file/excel_normal_100k_records.xlsx";
normalXLSXPopulateTest(pth);
