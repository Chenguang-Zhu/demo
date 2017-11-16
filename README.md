# demo

### To run the script [run_all.py](https://github.com/Chenguang-Zhu/demo/blob/master/scripts/run_all.py):

#### Requirements
Python 3.4+  
JDK 1.7+  
Maven 3.0 or later  
Internet connection  

#### On Linux
0. Setup environment before you start:  
    Make sure your environment variables `JAVA_HOME` (for Java) and `M2_HOME` (for Maven) are set correctly according to the instructions. 

1. Create a directory named `projects` in your home directory (`~`):  
    `cd ~`  
    `mkdir projects`  
    
2. Clone the [CSlicer](https://bitbucket.org/liyistc/gitslice/src/ba2f3af1af16ddd98bef31274087681d1c396d07/?at=master) repository in the `projects` directory:  
    `cd ~/projects`  
    `git clone https://bitbucket.org/liyistc/gitslice.git`  

3. (Optional: do this step only if you want to run [Definer](https://bitbucket.org/liyistc/gitslice/src/f978857b4d8d97328eefc21cd39f8d820075a677/?at=opt)) Checkout to `opt` branch:  
    `cd ~/projects/gitslice`  
    `git checkout opt`  

4. Setup external dependencies:  
    `cd ~/projects/gitslice`  
    `git submodule init`  
    `git submodule update`  

5. Build CSlicer (Definer):  
    `cd ~/projects/gitslice`  
    `mvn install -DskipTests`  
    
2. Clone the [demo](https://github.com/Chenguang-Zhu/demo) repository in the `projects` directory:  
    `cd ~/projects`  
    `git clone https://github.com/Chenguang-Zhu/demo.git`  
    
3. Clone the [DoSC](https://github.com/Chenguang-Zhu/DoSC) dataset repository in the `projects` directory:  
    `git clone https://github.com/Chenguang-Zhu/DoSC.git`  
    
4. Run the script [genconfigs.py](https://github.com/Chenguang-Zhu/demo/blob/master/scripts/genconfigs.py) to update all the configuration files to reflect the path on your machine:  
    `cd ~/projects/demo/scripts`  
    `./genconfigs.py`  
    
5. Create directories for storing Definer logs and Maven logs:  
     `cd ~/projects/demo/_results`  
     `mkdir definer`  
     `mkdir mvn`  
     
6. Run the script [run_all.py](https://github.com/Chenguang-Zhu/demo/blob/master/scripts/run_all.py):  
     `cd ~/projects/demo/scripts`  
     `./run_all.py`  
     
