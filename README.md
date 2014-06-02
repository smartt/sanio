**I'm not currently maintaining this project. If you need simple text cleaning without the I/O chaining, you might like my other project: https://github.com/smartt/sanity**

SANIO IS A WORK IN PROGRESS THAT COULD EXPERIENCE MAJOR REFACTORING AND REDESIGN!! YMMV UNTIL IT STABALIZES

Possibly dependencies (depending on what you're doing):

 - chardet (character-type detection.) I'm using version 1.0.1.
 - xlrd (for reading/writing Excel files.) I'm using something like 0.7.6.

## Sanio Tool Chain
Sanio features a collection of "chainable" tools for reformatting and translating input data into something more enjoyable to work with.  Furthermore, Sanio offers a pattern for extending these tools to add your own, unique steps to your data-processing pipeline.

At the core, every Sanio object (that inherits from BaseSanio) is a cleaner, filter, reader, validator, writer, and a data_source.  Because the tools all share common interfaces, they can be chained together.

Sanio's tools are spread accross the following categories:

 - Aggregators
 - Cleaners
 - Filters
 - Readers
 - Transformers
 - Validators
 - Writers 

### Aggregators
Aggregators analyze entire rows or columns of data.  They can compute averages, min/max, sums, and other values.  They are generally used to create (or insert) new data based on input data.

### Cleaners
Cleaners manipulate data to ensure a consistent format.  A Cleaner might convert between character encodings, capitalize strings, or simply trim off white-space.

### Filters
Filters are used to remove rows, columns, or cells of data using the boolean response from a function.

### Mappers
Mappers map functions to columns or cells.

### Readers
Readers know how to obtain data from a particular source (i.e., a file or URL), or extract data stored in various formats (i.e., CSV, XML, XLS, etc.), and normalize it for use by other Sanio tools in the chain.

### Transformers
Transformers can reshape the data.  They let you change the structure (even if the change is as simple as renaming a column.)

### Validators
Validators can be used for basic data analysis.  They are easily chained to Filters.

### Writers
Writers take normalized, Sanio data and put it somewhere else (i.e., a file, a
socket, etc.)


## Examples
### Reading a CSV
Let's start with a simple example:

You have a CSV file on disk (`input.csv`), and you'd like a Python dictionary
instead.  (Yes, Python has `csv.DictReader`, but bear with me -- we'll get to the fun stuff quickly):

```
the_data_as_a_dict = CSVReader(data_source=FileReader('input.csv'))
```

If your data was online, you might use the HTTPReader instead:

```
the_data_as_a_dict = CSVReader(data_source=HTTPReader('http://example.com/input.csv'))
```

### Converting CSV to JSON
The examples above transformed CSV input into a Python Dictionary in memory.  This time, we'll take a different approach, and convert the data into JSON instead while writing it back to disk:


```
FileWriter(
    'output.json',
    data_source=JSONWriter(
        data_source=CSVReader(
            data_source=FileReader('input.csv')
        )
    )
)
```

You'll notice an interesting pattern here.  Sanio's tools are designed to be patched-together by chaining the input from one tool to the output of another.  This is typically done by passing Sanio tools as "readers".


### Using Mappers

Mappers allow you to manipulate data as it flows through the pipe by mapping functions to data.  The main mapper is `FuncMapper`.  FuncMapper can be used to process each field of data through a single function using a function-pointer on initialization:

```
FileReader(
    'foo.txt',
    cleaner=FuncMapper(my_processing_function)
)
```

FuncMapper can also expand the function pointer concept by taking a Dictionary of column-names and function pointers instead.  This allows you to map different parts of your data using different functions.  For example, you might map a date field to convert it into a Python Date object, while mapping a currency field to convert it to a Python Decimal in a different currency.

Let's use the following CSV data (included as "sanio/parsers/test_data/numbers.csv" in the source of the Python library) as an example:

```
"SMBL","Price","Date","Time","Day Change","Open","High","Low","Volume"
"AAPL",587.92,"4/30/2012","1:54pm",-15.08,597.94,598.40,584.75,12244871
"GOOG",607.89,"4/30/2012","1:55pm",-7.09,612.99,616.082,607.67,1022507
"NFLX",80.56,"4/30/2012","1:56pm",-3.18,82.61,83.8723,80.10,4504323
```

Let's say that we wanted to convert each company's ticker symbol into their company name on import.  First we would implement a function to convert symbols into company names, and then pass a function pointer to said function to the cleaner:

```
def company_name_for_ticket_symbol(smbl):
	...do some lookups...
	return company_name

data = CSVReader(
	data_source=FileReader('numbers.csv'),
	cleaner=FuncMapper(company_name_for_ticket_symbol)
)
```


----

### -- END OF USEFUL DESCRIPTIONS. ON TO RANDOM EXAMPLES --

----

Downloading a file:

```
FileWriter(
	'index.html',
	data_source=HTTPReader('http://google.com/')
)
```

Example dealing with NULL byte errors:


```
data = CSVReader(
		data_source=FileReader(
				'files/SOME_DATA.CSV',
				cleaner=FuncMapper(StringCleaner.remove_null_bytes)
		)
	)
```


Pull some data from a CSV, but skip lines with an empty 'Price' field:

```
data = CSVReader(
			data_source=FileReader('files/SOME_DATA.CSV'),
			filter=RowFilter('Price', function=StringValidator.is_empty)
		)
```

Get RSS posts whose titles don't contain the word "links":

```
data = RSSReader(
			data_source=HTTPReader('http://some.blog.foo/feed/'),
			filter=RowFilter('Title', function=lambda x: x.lower().find('links') < 0)
		)
```


LICENSE
=======
Copyright (c) 2012, Erik Smartt
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list
of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
