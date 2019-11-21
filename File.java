package main;

public class File {
 public int group=-1;
 public int members[];
 public int member_num=0;
 public int turn=0;
 public int isleader=0;
 public File(int size,int index) 
 {//constructor
	 this.members=new int[size];
	 this.members[this.member_num++]=index;
 }//constructor
}
