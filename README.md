# Address Cleansing Demo
Demo for using AI to cleanse the address

## prompt
- Generate the address with the random format
  - `Please provide three Canadian addresses in English, including apartment or street numbers, street names, provinces, country, postal codes, and any other relevant information. Please feel free to mix up the format and leave out some details to simulate realistic handwriting. Each address should be written on a separate line.`
- Cleanse the random addresses generated by the first step
  - `Please provide the address details in the following format: Number, Street or District, City, Province, Country, and Postcode. The output should be in JSON format: [{},{}]:`
