# lookup-norway

A repository of journalist's lookup tables related to **Norwegian public data**. Designed for programmatic access using tools such as [agate-lookup](https://github.com/wireservice/agate-lookup).

Anyone may contribute a lookup table by sending a pull request to this repository.

This work is inspired and partly copied from the original [lookup service](https://github.com/wireservice/lookup)

###Lookup tables available: 

* `kommunenr` - Let's you find the corresponding municipality name (kommune) to the municipality id (kommunenr)

## Structure of files

Each folder is a key that can be used for a lookup. Within that folder are CSV files. The name of the CSV file is the name of the value that it maps to. The CSV itself will contain two columns, one with the key and another with the value. For example, `kommunenr/kommune.csv` contains a CSV file that looks like this:

```
kommunenr,kommune
0101,Halden
0104,Moss
0105,Sarpsborg
0106,Fredrikstad
...
```


## Metadata format

Each CSV table must be accompanied by a YAML file. That file must have an identical filename, plus the `.yml` extension. For example, the table `fips/state.csv` must be accompanied by `fips/state.csv.yml`. This file should contain the following metadata:

```yaml
data: A description of the data, including any notes necessary to use it correctly.
version: A description of the specific version of the data.
sources:
  - A list of sources for the data, such as "United States Census Bureau", including URLs whenever possible
contributors:
  - The name <and email of anyone who has contributed to this table>
columns:
  key_column_name:
    name: Human readable name for this column
    type: Agate column type, such as "Text" or "Number"
  value_column_name:
    name: Human readable name for this column
    type: Agate column type, such as "Text" or "Number"
```

See `kommunenr/kommuner.csv.yaml` for an example of a complete metadata file.

## Rules for including data

Anyone may submit a pull request to add a table to this repository, however, the following rules will guide inclusion of any data:

* The data must have journalistic value.
* The data must be from an authoritative source.
* The CSV must be in "standardized" CSV format. (Run through [in2csv](http://csvkit.readthedocs.org/en/latest/scripts/in2csv.html).)
* All keys must be unique. (No split/combine crosswalks.)
* All keys must be durable identifiers, not names.
* All filenames and keys must use `snake_case`.
* Periods must not be used in filenames or keys except as defined above.
* Four digit years must be used everywhere.
* Each CSV must be 250KB or less.

## I found an error!

If people are going to rely on the tables in this dataset then there must be a log every error. If you find an error in any data, please send a pull request with a correction. That same pull request must also add an entry to `ERRORS.md` describing precisely the nature of the error.
