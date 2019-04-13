Every folder corresponds to one task
- factorial-full -> The dataset consists of factorial program
- factorial-loop -> dataset consists of only the loop of the factorial program
- arithmetic-full -> dataset consists of arithmetic operations performed repeatedly

To generate data: Do `cd $task-directory` followed by `sh init.sh` 

Data will be generated in 2 files: data.npy (for features), labels.mpy (for labels)

For fast experimentation, there is delete.sh file which deletes the data and allows you 
to make changes to the dataset generation process (like chnaging the umber of unrolls)
To delete all the data and return the directory to the initial state:
sh delete.sh

Models are stored in colab notebooks

The google CoLab links are as follows:
- Arithmetic model : https://colab.research.google.com/drive/1E0vnDD3R3U3bWuhJlTbEw1b1HtsfOUiF
- Factorial model : https://colab.research.google.com/drive/1RuMabeBsgiYOjlXzQmwEsO_jNThWNmPQ