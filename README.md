# fileSplitter
<p>A command line Python script to split files into n chunks or join n chunks into a file.</p>
<p>usage: fileSplitter.py [-h] [-f File Path] [-c Chunk Size | -n n_parts] MODE</p>
<p></p>
<p>positional arguments:</p>
  <p>MODE           <b>split</b> or <b>join</b></p>

<p>optional arguments:</p>
  <p>-h, --help     show this help message and exit</p>
  <p>-f <b>File Path</b>   Path to file that will be splited.</p>
  <p>-c <b>Chunk Size</b>  Chunk size in bytes.</p>
  <p>-n <b>n_parts</b>     Number of parts in which the file will be splited.</p>
  <p></p>
  <p>To join files, one must run the script from a directory that has all the files to be joined and nothing else.</p>
