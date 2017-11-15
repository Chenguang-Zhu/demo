# demo

### To run the script [run_all.py](https://github.com/Chenguang-Zhu/demo/blob/master/scripts/run_all.py):

#### Requirements
Python 3.4+  
JDK 1.7+  
Maven 3.0 or later  
[CSlier](https://bitbucket.org/liyistc/gitslice/src/ba2f3af1af16ddd98bef31274087681d1c396d07/?at=master) or [Definer](https://bitbucket.org/liyistc/gitslice/src/f978857b4d8d97328eefc21cd39f8d820075a677/?at=opt) binary distribution  
Internet connection  

#### On Linux
1. Create a directory named `projects` in your home directory (`~`):  
    `cd ~`  
    `mkdir projects`  
2. Clone the [demo](https://github.com/Chenguang-Zhu/demo) repository in the `projects` directory:  
    `cd ~/projects`  
    `git clone https://github.com/Chenguang-Zhu/demo.git`  
3. Clone the DoSC dataset repository in the `projects` directory:  
    `git clone https://github.com/Chenguang-Zhu/DoSC.git`  
4. Run script [genconfigs.py](https://github.com/Chenguang-Zhu/demo/blob/master/scripts/genconfigs.py) to update all the configuration files to reflect the path on your machine:  
    `cd ~/projects/demo/scripts`  
    `./genconfigs.py`  
5. Create directories for storing Definer logs and Maven logs:  
     `cd ~/projects/demo/_results`  
     `mkdir definer`  
     `mkdir mvn`  
6. Run the script [run_all.py](https://github.com/Chenguang-Zhu/demo/blob/master/scripts/run_all.py):  
     `cd ~/projects/demo/scripts`  
     `./run_all.py`  
