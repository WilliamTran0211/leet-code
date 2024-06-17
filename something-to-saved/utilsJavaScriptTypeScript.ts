export default function guessDelimiter(buffer) {
  /*
  Import the buffer string of the CSV file, take a sample row (limited by a specified number) from that file, and return the guessed result of the delimiter. 
  If no delimiters are found in the file, it will default to returning a comma as the delimiter.
  */
  const VALID_DELIMITERS = [",", ";", "\t", "|"];
  const PRIORITY_DELIMITER = ",";
  const SAMPLE_LIMIT = 5;

  const csvData = buffer.toString().split("\n");

  const csvHeaders = csvData.slice(1, SAMPLE_LIMIT);

  const canBeDelimiter: Record<string, number> = {};

  // Count the delimiters in the sample rows, which are unified into a single string.
  for (let delimiter of VALID_DELIMITERS) {
    const ref = (
      csvHeaders.join("").match(new RegExp("\\" + delimiter, "g")) || []
    ).length;
    canBeDelimiter[delimiter] = ref;
  }

  // Compare the values of the counted delimiters; return those that appear more frequently. If there is no delimiter than return results = {"" : -infinity}
  const resultGuessing = Object.keys(canBeDelimiter).reduce(
    (acc, key) => {
      return canBeDelimiter[key] > acc.value
        ? { value: canBeDelimiter[key], key }
        : acc;
    },
    { value: -Infinity, key: "" }
  );

  return resultGuessing.key ? resultGuessing.key : PRIORITY_DELIMITER;
}
