const IntegerContainerInterface = require("./integerContainerInterface");

class IntegerContainer extends IntegerContainerInterface {
  constructor() {
    super();
    // create container list
    this.container = [];
  }

  add(value) {
    // add value to container
    this.container.push(value);
    // return new container length
    return this.container.length;
  }

  delete(value) {
    // find index of value in container
    const index = this.container.indexOf(value);
    console.log(index);

    // if value present remove value and return true
    if (index !== -1) {
      let newList = this.container.splice(index, 1);
      console.log(newList);
      return true;
    }

    // value not present return false
    return false;
  }

  getMedian() {
    /* * Should return the median integer - the integer in the middle
     * of the sequence after all integers stored in the container
     * are sorted in ascending order.
     * If the length of the sequence is even, the leftmost integer
     * from the two middle integers should be returned.
     */

    // return null if container is empty
    if (this.container.length === 0) {
      return null;
    }

    // sort in asc order
    this.container.sort(function (a, b) {
      return a - b;
    });

    // if length is even return the left most integer of the two middle numbers
    if (this.container.length % 2 === 0) {
      return this.container[this.container.length / 2 - 1];
    }
    // two pointer method to loop through array to get to the center
    let left = 0;
    let right = this.container.length - 1;

    while (left <= right) {
      if (left == right) return this.container[left];
      left++;
      right--;
    }
  }
}

module.exports = IntegerContainer;

function getValue(x) {
  // return null if value doesn't exist
  return x ?? null;
}

class RecordManager {
  constructor() {
    this.record = {};
  }

  updateRecord(key, field, value, deleteField) {
    if (!this.record[key]) this.record[key] = {};
    if (typeof value !== "number") throw new Error("Value must be an integer");
    if (deleteField) {
      if (this.record[key][field]) {
        delete this.record[key][field];
        if (Object.keys(this.record[key]).length === 0) {
          delete this.record[key];
        }
      }
    } else {
      this.record[key][field] = (this.record[key][field] || 0) + value;
    }
  }

  getRecord(key, field) {
    if (!this.memory[key] || typeof this.memory[key] !== "object") {
      console.log("Key not found in memory or not an object");
      return null;
    }
    return this.memory[key][field] ?? null;
  }

  delete(key, field) {
    if (this.record[key] && this.record[key][field]) {
      delete this.record[key][field];
    }
  }
}

function updateRecordField(data, key, field, value) {
  if (!data[key]) {
    data[key] = {};
  }

  if (!data[key][field]) {
    data[key][field] = value;
  } else {
    data[key][field] += value;
  }

  return data[key][field];
}
