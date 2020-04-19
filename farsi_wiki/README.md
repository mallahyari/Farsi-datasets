# Farsi Wiki Dataset

This dataset has been extracted from the Farsi Wikipedia dump (`fawiki-20181001-corpus.xml.bz2`) available at [linguatools](https://linguatools.org/tools/corpora/wikipedia-monolingual-corpora/). This file contains the _articles textual content_ along with the _categories_ of each article (if available). Every line of this dataset represent a single Farsi Wikipedia page and has the following format:

```
text.[categories]
```

- `Catetories` is a list of category names assigned to each article.

- Text of each article has been somewhat cleaned (i.e. html tags removed, etc), but should be further preprocessed.

## License

This file has been derived from an XML version of the original Wikipedia and are therefore made available under the same license as Wikipedia itself: [Creative Commons Attribution-ShareAlike](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

## Contributions

If you are interested in contributing, please send me an email at `mallahyari@georgiasouthern.edu`.
