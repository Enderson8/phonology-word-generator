# Phonology Word Generator

A simple Python application that generates fictional words based on customizable phonological rules.

## Features

- Generate words with a custom number of syllables
- Optional consonant clusters
- Optional vowel clusters
- Random phonological generation
- Easy to extend with new phonological rules

## Example

```
Number of syllables: 4
Allow consonant clusters? yes
Allow vowel clusters? no

Generated word:
kratenomu
```

## Requirements

- Python 3.14 or newer

## Running

```bash
python gerador_palavras.py
```

## Building an executable

```bash
python -m PyInstaller --onefile gerador_palavras.py
```

## Roadmap

- [ ] Syllable templates (CV, CVC, CCV...)
- [ ] Diphthong and triphthong support
- [ ] Realistic consonant clusters
- [ ] Different phonological families
- [ ] Graphical user interface
- [ ] Export generated words

## License

This project is licensed under the MIT License.
