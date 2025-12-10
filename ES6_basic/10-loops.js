export default function appendToEachArrayValue(array, appendString) {
  const arrayValue = []
    for (const value of array) {
    arrayValue.push(appendString + value)
  }

  return arrayValue;
}
