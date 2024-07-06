# YAML

YAML (YAML Ain't Markup Language) is a human-readable data serialization standart that is commonly used for configuration files in software applications, defining API and web service specifications, storing and organizing metadata and content structure, data serialization and exchange between programming languages, and Infrastructure as Code (IaC) in DevOps and cloud-native environments. Their human-readable format, flexibility, and widespread adoption across various domains make YAML a versatile language for configuration management, documentation, automation, and scripting tasks.

**Example**
```yaml
database:
  host: "localhost"
  port: 5432
  username: "admin"
  password: "secret"
```

## Key Features

- **Human-readable**: YAML is designed to be easy to read and write.
- **Data serialization**: It can serialize data structures like lists, dictionaries, and scalars.
- **Language-agnostic**: YAML can be used with any programming language.
- **Indentation-based**: Uses indentation to represent structure, similar to Python.

## Basic Syntax

### Scalars

Scalars are the simplest form of data in YAML. They can be strings, numbers, or booleans.

```yaml
string: "Global Equities"
integer: 100000
float: 3.14
boolean: true
```
### Lists
Lists are collections of items. Each item in a list is prefixed with a hyphen (-).

```yaml
Sectors:
  - Materials
  - Consumer Discretionary
  - Information Technology
```

### Dictionaries
Dictionaries (or mappings) are collections of key-value pairs.
```yaml
fund:
  name: XYZ Systematic Equities Fund
  investment horizon: 5
  volatility: High
```

### Nested Structures
YAML supports nested lists and dictionaries.
```yaml
stocks:
  - name: TLSA
    last price: 173.63
  - name: AMD
    last price: 168.34
```
### Comments
Comments in YAML are denoted by the # symbol.

```yaml
# This is a comment
ticker: GS  # Inline comment
```

### Example
The start of a YAML document is denoted by three dashes '---'.

```yaml
# Exchange Rates Configuration
---
metadata:
  description: Exchange rates configuration for various currencies
  version: 1.0.0
  lastUpdated: "2024-06-07"

baseCurrency: USD

exchangeRates:
  - currency: EUR
    rate: 0.92
    description: Euro
  - currency: GBP
    rate: 0.81
    description: British Pound
  - currency: JPY
    rate: 139.75
    description: Japanese Yen
  - currency: AUD
    rate: 1.48
    description: Australian Dollar
  - currency: CAD
    rate: 1.34
    description: Canadian Dollar
  - currency: CHF
    rate: 0.91
    description: Swiss Franc
  - currency: CNY
    rate: 6.91
    description: Chinese Yuan Renminbi
  - currency: HKD
    rate: 7.75
    description: Hong Kong Dollar
  - currency: NZD
    rate: 1.62
    description: New Zealand Dollar
  - currency: SEK
    rate: 10.38
    description: Swedish Krona

updateFrequency: daily

```



## Best Practices
- **​Consistent indentation**​: Use spaces instead of tabs for indentation.
- **​Avoid special characters**​: Use quotes around strings that contain special characters.
-  **Use comments**​: Add comments to make the YAML file easier to understand.


## Relevance in Finance

Common practice in software engineering is to use YAML files to store confiurations and setting paramaters, we can extend this concept to financial data analysis where we will use YAML config files to help to automate reporting[placeholder].