# Sanio makes your input files sane to work with

THIS IS A WORK IN PROGRESS!!


## Tool Types
Sanio feature five types of tools for reformatting and translating input data into something more enjoyable to work with.  These are: Readers, Parsers, Cleaners, Transformers, and Writers:

### Readers
Readers know how to obtain data from a particular source (i.e., a file or URL),
and output said data when iterated over.

### Parsers
Parsers are generally 'converters' -- they pull data from a reader, parse it,
and return the parsed data as a Python Dictionary when iterated over.

### Cleaners
Cleaners take function pointers, and map said functions over data via their
`clean()` method.

### Transformers
Take a Python Dictionary and output a different format (i.e., JSON, XML, etc.)

### Writers
Writers take data from an iterator and put it somewhere else (i.e., a file, a
socket, etc.)


## Examples
### Reading a CSV
Let's start with a simple example:

You have a CSV file on disk ('input.csv'), and you'd like a Python dictionary
instead.  (Yes, Python has `csv.DictReader`, but this example sets the tone):

```
the_data_as_a_dict = CSVParser(reader=FileReader('input.csv'))
```

If your data was online, instead of locally, you might use the (currently fictional) URLReader instead:

```
the_data_as_a_dict = CSVParser(reader=URLReader('http://example.com/input.csv'))
```

### Converting CSV to JSON
The examples above transformed CSV input into a Python Dictionary in memory.  This time, we'll take a different approach, and convert the data into JSON instead while writing it back to disk:


```
FileWriter(
    'output.json',
    reader=JSONTransform(
        reader=CSVParser(
            reader=FileReader('input.csv')
        )
    )
)
```

You'll notice an interesting pattern here.  Sanio's tools are designed to be patched-together by chaining the input from one tool to the output of another.  This is typically done by passing Sanio tools as readers.


### Using Cleaners

Cleaners allow you to manipulate data as it flows through the pipe by mapping functions to data.  There are two main cleaners:  `FuncCleaner` and `FuncDictCleaner`.  FuncCleaner is used to process each field of data through a single function.  It takes a function-pointer on initialization, like this:

```
FileReader(
    'foo.txt',
    cleaner=FuncCleaner(my_processing_function)
)
```

FuncDictCleaners expand the function pointer concept by taking a Dictionary of column-name/keys/labels and function pointers.  This allows you to map different parts of your data using different cleaning functions.  For example, you might map a date field to convert it into a Python Date object, while mapping a currency field to convert it to a Python Decimal in a different currency.

Let's use the following CSV data (included as "sanio/parsers/test_data/numbers.csv" in the source) as an example:

```
"SMBL","Price","Date","Time","Day Change","Open","High","Low","Volume"
"AAPL",587.92,"4/30/2012","1:54pm",-15.08,597.94,598.40,584.75,12244871
"GOOG",607.89,"4/30/2012","1:55pm",-7.09,612.99,616.082,607.67,1022507
"NFLX",80.56,"4/30/2012","1:56pm",-3.18,82.61,83.8723,80.10,4504323
```

Let's say that we wanted to convert each company's ticker symbol into their company name on import.  First we would implement a function to convert symbols into company names; and then pass a function pointer to said function to the cleaner, like this:

```
    def company_name_for_ticket_symbol(smbl):
        ...do some lookups...
        return company_name

    data = CSVParser(
                reader=FileReader('numbers.csv'),
                cleaner=FuncCleaner(company_name_for_ticket_symbol)
           )
```





Example dealing with NULL byte errors:

```
    data = CSVParser(
                reader=FileReader('exitfiles/NKK_20120430_ORDER.CSV'
           )
```

```
_csv.Error: line contains NULL byte
```

```
    data = CSVParser(
                reader=FileReader('exitfiles/NKK_20120430_ORDER.CSV',
                cleaner=FuncCleaner(StringCleaner.remove_null_bytes))
           )
```




```
>>> parser = CSVParser(reader=FileReader('test_data/simple.csv'), cleaner=FuncDictCleaner({'c': BaseCleaner.safe_int}))

>>> [i for i in parser]
[{'a': 'one', 'c': 3, 'b': 'two'}]
```

```
>>> parser = CSVParser(reader=FileReader('test_data/numbers.csv'))

>>> [i['SMBL'] for i in parser]
['AAPL', 'GOOG', 'NFLX']

>>> parser = DictTransform(reader=CSVParser(reader=FileReader('test_data/numbers.csv')), remap_fields={'SMBL': 'Symbol'})

>>> [i['Symbol'] for i in parser]
['AAPL', 'GOOG', 'NFLX']

>>> [i['Symbol'] for i in DictTransform(reader=CSVParser(reader=FileReader('test_data/numbers.csv')), remap_fields={'SMBL': 'Symbol'})]
['AAPL', 'GOOG', 'NFLX']

```
