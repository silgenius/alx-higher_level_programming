#!/usr/bin/node
// a script that searches the second biggest integer
// in the list of arguments.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  // Extract arguments, skip first two elements which are 'node' and the script name
  const args = process.argv.slice(2).map(Number);

  // Find the unique elements and sort them in descending order
  const uniqueArgs = [...new Set(args)].sort((a, b) => b - a);

  // Print the second largest element if there are at least two unique elements
  if (uniqueArgs.length < 2) {
    console.log(0);
  } else {
    console.log(uniqueArgs[1]);
  }
}
