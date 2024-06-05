# JSON 

JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is recognisable by the use of curly brackests. JSON is built on two structures:

1. **A collection of name/value pairs**: In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array. In python this is a dictionary.
2. **An ordered list of values**: In most languages, this is realized as an array, vector, list, or sequence.

Here is an example of a JSON object:

```json
{
    "fund": "Jane Doe Capital",
    "horizon": 7,
    "is_open": true,
    "fum": 4000000,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA"
    },
    "phone_numbers": ["123-456-7890", "987-654-3210"]
}
```

## Key Features

- **​Structured Data Representation​**: JSON's ability to represent hierarchical data makes it an ideal format for storing and transmitting financial data.
- **Interoperability​**: JSON is language-independent but uses conventions that are familiar to programmers of the C family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. This makes JSON a versatile format for exchanging data between different systems and applications.
- **​Ease of Use​**: JSON is easy to read and write, which simplifies the process of data entry and review. This is particularly useful in financial contexts where accuracy and clarity are paramount.
- **​APIs and Web Services​**: Many financial services and APIs use JSON as their primary data format for communication. For example, financial market data providers often offer JSON-based APIs to access real-time stock prices, historical data, and other financial metrics.
- **Data Storage and Retrieval​**: JSON is commonly used in NoSQL databases like MongoDB, which are often employed for storing large volumes of data. These databases can efficiently store and query JSON documents, making them suitable for applications that require quick access to data.
Example: Storing Financial Data in JSON


## Relevance to Financial Data

JSON is a powerful and flexible format for storing and exchanging  data. Its human-readable structure, ease of use, and compatibility with various programming languages and systems make it an excellent choice for data storage for many applications and databases. Given this, the most frequent use of JSON for financial analysis is sending and receiving data from [APIs](`What Are APIs.md`)