# SearchAtHome
Microcomputer-based environment for run-time SBSE research projects

## SSBSE20

The environment uses Raspberry Pi 3B and 4B devices, some of which are equipped with a Sense hat (at one point the Sense hat LED array displayed run status).  Developed for Python 3.7 and uses the [helloevolve.py Gist](https://gist.github.com/josephmisiti/940cee03c97f031188ba7eac74d03a4f) as a sample GA.

To run the full experiment:

* `bash string-runner.sh` -- tweaking `string-runner.sh` for whichever device you're experimenting upon.

To run a single experiment:

* `python3 string-search.py [seed]`  

## Data parsing

The raw data from our experiment is in the tarball within the `data` directory.  Untar that, run `string-ga-parser.py` against it to generate the CSV file, and then import into R.

## Hardware

* Raspberry Pi 4B (4GB RAM)

* Raspberry Pi 3B x2 (additional Pi was for redundancy)

* Acer Aspire One netbook (acts as a 'point of entry' to a sandboxed network)

* Linksys WRT router (installed with [Tomato firmware](https://www.polarcloud.com/tomato))
