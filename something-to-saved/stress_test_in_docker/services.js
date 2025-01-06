import * as xlsx from "xlsx";
import * as JSONStream from "JSONStream";
import XlsxPopulate from "xlsx-populate";
import { createReadStream, readFileSync, unlinkSync } from "fs";
import { tmpdir, type } from "os";
import { join } from "path";
import { Readable, Transform } from "stream";
import es from "event-stream";
import ExcelJS from "exceljs";

function bufferToStream(buffer) {
  var stream = new Readable();
  stream.push(buffer);
  stream.push(null);
  return stream;
}

export async function convertToXlsxBuffer(extension, buffer) {
  try {
    console.log("convertToXlsxBuffer calling ", { extension, buffer });
    console.log("Memory usage before processing:", process.memoryUsage());
    const workBook = xlsx.read(buffer, { cellHTML: false });
    buffer = xlsx.write(workBook, {
      bookType: extension,
      bookSST: true,
      type: "buffer",
    });
    console.log("Memory usage after processing:", process.memoryUsage());
    return buffer;
  } catch (error) {
    console.error("Error in convertToXlsxBuffer:", error);
    throw error;
  }
}

export async function convertUseXlsxPopulate(extension, buffer) {
  let result;
  await XlsxPopulate.fromDataAsync(buffer).then((wb) => {
    result = wb.outputAsync();
  });

  return result;
}

export async function convertToXlsxBuffer23(extension, buffer) {
  try {
    console.log("convertToXlsxBuffer calling ", { extension, buffer });
    console.log("Memory usage before processing:", process.memoryUsage());

    // Create a readable stream from the buffer
    const readable = new Readable();
    readable._read = () => {}; // No-op
    readable.push(buffer);
    readable.push(null);

    // Read the workbook from the stream
    const workBook = xlsx.stream.set_readable(readable, { cellHTML: false });

    // Write the workbook to a buffer
    const outputBuffer = xlsx.write(workBook, {
      bookType: extension,
      bookSST: true,
      type: "buffer",
    });

    console.log("Memory usage after processing:", process.memoryUsage());
    return outputBuffer;
  } catch (error) {
    console.error("Error in convertToXlsxBuffer:", error);
    throw error;
  }
}

export async function convertXlsx(filename = "", inputBuffer) {
  console.log("convertXlsx calling");

  return new Promise((resolve, reject) => {
    try {
      const buffers = [];
      const stream = Readable.from(inputBuffer);

      stream.on("data", function (data) {
        buffers.push(data);
      });

      stream.on("end", function () {
        // let buffer = buffers;
        // const workbook = xlsx.stream.read(buffer);
        // buffer = xlsx.write(workbook, {
        //   bookType: "xlsx",
        //   bookSST: true,
        //   type: "buffer",
        // });
        // resolve(buffer);
        // const options = {
        //   filename: filename,
        //   bookType: "xlsx",
        //   useStyles: true,
        //   useSharedStrings: true,
        //   type: "buffer",
        // };
        // const workbook = new ExcelJS.stream.xlsx.WorkbookWriter(
        //   options,
        //   buffers
        // );
        // resolve(workbook);
      });

      stream.on("error", function (error) {
        reject(new Error(error));
      });
    } catch (error) {
      console.error(error);
      reject(new Error(error));
    }
  });
}

export async function convertXlsxBufferTmpLocalFile(extension, buffer) {
  try {
    const tmpDir = tmpdir();
    const tempFilePath = join(tmpDir, `tempfile.${extension}`);
    const workBook = xlsx.read(buffer, { cellHTML: false });
    xlsx.writeFile(workBook, tempFilePath, {
      bookType: extension,
      bookSST: true,
    });

    const resultBuffer = readFileSync(tempFilePath);
    unlinkSync(tempFilePath); // Clean up the temporary file
    return resultBuffer;
  } catch (err) {
    console.error(err);
  }
}

export async function readStreamReadable(extension, buffer) {
  const tmpDir = tmpdir();
  const tempFilePath = join(tmpDir, `tempfile.${extension}`);
  const stream = createReadStream(tempFilePath);
}

export async function convertToXlsxChunkBuffer(extension, buffer) {}

export async function addingData(buffer) {
  XlsxPopulate.fromDataAsync(buffer).then((wb) => {
    const sheet = wb.sheet("Sheet1");
    const newColumn1Index = 4;
    const totalColumn = sheet.usedRange().endCell().columnNumber(); // Define totalColumn
    //get old file WIDTH
    let templateColumnWidth = [];
    for (let i = 1; i <= totalColumn; i++) {
      if (i === newColumn1Index) {
        const index = i == 1 ? 1 : i;
        templateColumnWidth.push(sheet.column(index).width());
      }
      templateColumnWidth.push(sheet.column(i).width());
    }

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

    sheet.cell("A1").value(newRangeFromRow);

    for (let i = 0; i <= totalColumn + 1; i++) {
      sheet.column(i + 1).width(templateColumnWidth[i]);
    }
  });

  return buffer;
}

export async function readStreamJson(fileBuffer) {
  return new Promise((resolve, reject) => {
    const stream = Readable.from(fileBuffer);
    const pipeline = stream.pipe(JSONStream.parse());

    let result = [];
    pipeline.on("data", (data) => {
      result.push(data);
    });

    pipeline.on("end", () => {
      resolve(result);
    });

    pipeline.on("error", (error) => {
      reject(error);
    });
  });
}

export async function readStreamJson2(fileBuffer) {
  // const prom = await new Promise((resolve, reject) => {
  //   try {
  //     let result = [];
  //     const stream = Readable.from(fileBuffer);
  //     const pipeline = stream.pipe(JSONStream.parse());

  //     pipeline.on("data", (data) => {
  //       try {
  //         result = data;
  //       } catch (error) {
  //         reject(new Error(error));
  //       }
  //     });
  //     pipeline.on("end", () => {
  //       resolve(result);
  //     });
  //   } catch (error) {
  //     reject(new Error(error));
  //   }
  // });
  // return prom;

  const prom = await new Promise((resolve, reject) => {
    let result = [];
    const stream = Readable.from(fileBuffer);
    const pipeline = stream.pipe(JSONStream.parse());

    pipeline.on("data", (data) => {
      result.push(data);
    });

    pipeline.on("end", () => {
      resolve(result);
    });

    pipeline.on("error", (error) => {
      reject(new Error(error));
    });
  });

  return prom;
}
