import express from "express";
import bodyParser from "body-parser";
import multer from "multer";
import statusMonitor from "express-status-monitor";

import * as services from "./services.js";

const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

const app = express();
const PORT = 5050;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(statusMonitor());

app.get("/hello", function (_, res) {
  const message = "Hello World";
  console.log("GET hello calling ", { message });
  res.status(200).json({ message });
});

app.post(
  "/file-upload-transform",
  upload.single("file"),
  async function (req, res) {
    console.log("POST file-upload-transform calling ");
    const file = req.file;

    const startTime = Date.now();
    const transformFile = await services.convertToXlsxBuffer23(
      "xlsx",
      file.buffer
    );
    const endTime = Date.now();
    const timeTaken = `${endTime - startTime} ms`;

    res.status(200).json({
      message: "File uploaded successfully",
      timeTaken,
      buffer: transformFile,
    });
    transformFile.fill(0);
    console.log("Memory usage after response:", process.memoryUsage());
  }
);

app.post(
  "/file-upload-transform1",
  upload.single("file"),
  async function (req, res) {
    console.log("POST file-upload-transform1 calling ");
    const file = req.file;

    const startTime = Date.now();
    const transformFile = await services.convertXlsx({
      filename: file.filename,
      inputBuffer: file.buffer,
    });
    const endTime = Date.now();
    const timeTaken = `${endTime - startTime} ms`;

    res.status(200).json({
      message: "File uploaded successfully",
      timeTaken,
      buffer: transformFile,
    });
    transformFile.fill(0);
    console.log("Memory usage after response:", process.memoryUsage());
  }
);

app.post("/json-upload", upload.single("file"), async function (req, res) {
  console.log("POST json calling ");
  const file = req.file;

  await services
    .readStreamJson(file.buffer)
    .then((result) => {
      res.status(200).json({ message: "File uploaded successfully", result });
    })
    .catch((error) => {
      res.status(500).json({ message: "Error in reading file", error });
    });
});

app.post("/json-upload2", upload.single("file"), async function (req, res) {
  console.log("POST json2  calling  ");
  const file = req.file;

  let result = [];
  try {
    result = await services.readStreamJson(file.buffer);
  } catch (err) {
    res.status(200).json({ message: "File uploaded successfully", result });
  }

  console.log({ result });
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
