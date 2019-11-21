package main;

import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;
import java.lang.reflect.Array;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;

public class new_2_2_close {
   static double[] df;
   static int dfn=0;
   static int D=398;
   static File[] files;
   static HSSFSheet tfdtsheet;
   static double lamda=0.5;
   static int ngroup=0;
   static int groups=398,thres=5,max_txt=398;
   static BufferedWriter bw;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		df=new double[20000];
		files=new File[398];
       String wfile="D:\\InformationTheoryGroupHomeWork\\words.xls";
       int sheet=0;
       String tfdt_file="D:\\InformationTheoryGroupHomeWork\\tfdt.xls";
		InputStream inputstream=new FileInputStream(tfdt_file);
    	HSSFWorkbook wb=new HSSFWorkbook(inputstream);
    	tfdtsheet=wb.getSheetAt(0);
    	
 	   String output="D:\\InformationTheoryGroupHomeWork\\ans.txt";
 	   FileOutputStream out=new FileOutputStream(output);
 	   OutputStreamWriter fs=new OutputStreamWriter(out);
 	   bw=new BufferedWriter(fs);
    	
         generate_df(wfile,sheet);
       // generate_distance("D:\\InformationTheoryGroupHomeWork\\distance.xls",0);
        _2_2closego();
        bw.close();
  	  	}
   public static void generate_df(String filename,int sheet) throws IOException 
    {//gf
	 	InputStream inputstream=new FileInputStream(filename);
    	HSSFWorkbook wb=new HSSFWorkbook(inputstream);
    	HSSFSheet sheeter=wb.getSheetAt(sheet);
    	for(int i=0;i<sheeter.getLastRowNum();i++) 
    	 {//for1
    		HSSFRow row = sheeter.getRow(i);
    		HSSFCell cell=row.getCell(1);
    		df[dfn++]=cell.getNumericCellValue();
    	 }//for1 
    	System.out.println(dfn);
    }//gf 
   public static double DKL(tdf a,tdf b) 
    {//DKL
	   double ans=0;
	   for(int i=0;i<a.length;i++)
	    {//for1
		   double wta=a.array[i]*(Math.log((double)D/df[i])/Math.log(2));
		   double wtb=b.array[i]*(Math.log((double)D/df[i])/Math.log(2));
		   //
		   if(wta==0||wtb==0) {
		   ans+=wta*(Math.log((wta+0.1)/(wtb+0.1))/Math.log(2));
		  // System.out.println("wta:"+wta+"wtb:"+wtb+"ans:"+ans);   
		   }else {
		   ans+=wta*(Math.log(wta/wtb)/Math.log(2));  	
		        }
	    }//for1
	       return ans;
    }//DKL
   public static tdf get_tdf(int index) 
    {//get_tdf
	   tdf ans=new tdf();
	   ans.array=new double[13000];
	   for(int j=0;j<files[index].member_num;j++)
	    {//for1
		   int row=files[index].members[j];
		   HSSFRow rower=tfdtsheet.getRow(row);
		   HSSFCell cell=rower.getCell(0);
		   String array[]=cell.getStringCellValue().split(",");
		    for(int i=0;i<array.length;i++)
		     {//for11
		    	ans.array[i]+=Integer.parseInt(array[i]);
		     }//for11
		       ans.length=array.length;
	    }//for1 
	   for(int k=0;k<ans.length;k++)
	    {//for2
		   ans.array[k]/=(double)files[index].member_num;
	    }//for2
	   return ans;
    }//get_tdf
   public static double calculate_distance(int a,int b) 
    {//cd
	   tdf tfa=get_tdf(a);
	   tdf tfb=get_tdf(b);
	  // System.out.println("tfa:"+tfa.length+"tfb:"+tfb.length);
	   tdf M=get_mix(tfa,tfb);
	   double distance = lamda*DKL(tfa,M)+(1-lamda)*DKL(tfb,M);
	   return distance;
    }//cd
   public static tdf get_mix(tdf a,tdf b) 
    {//gm
	   tdf ans=new tdf();
	   ans.array=new double[13000];
	   for(int i=0;i<a.length;i++)
	    {//for1
		   ans.array[i]=lamda*a.array[i]+(1-lamda)*b.array[i];
		   ans.length++;
	    }//for1
	   return ans;
    }//gm
   public static int findgroup(int index,int turn,int requester) throws IOException 
    {//findgroup
	   if(files[index].turn==turn)return -1;
	   if(files[index].group!=-1&&files[index].isleader==0)return -1;
	   files[index].turn=turn;
	   double mindistance=-1;
	   int target=-1;
	   double[] array=get_array(index);
	   for(int i=0;i<files.length;i++)
	    {//for1
		   if(i==index)continue;
		   if(files[i].group!=-1&&files[i].isleader==0)continue;
		   double distance;
		   if(files[i].group==-1) {
		    distance=array[i];
		       }else {
		    distance=get_distance(i,array); 	   
		       }
		   if(files[i].member_num>1) {//if42
		   //bw.write("distance:"+distance+"i:"+i+"membernum:"+files[i].member_num);
		    System.out.println("distance:"+distance+"i:"+i+"membernum:"+files[i].member_num);
		   }//if42
		   if(mindistance==-1) {//if1
			   mindistance=distance;
			   target=i;
		          }else if(distance<mindistance){//if1 if2
		       mindistance=distance;
		       target=i;
		          }//if2
	    }//for1
	   System.out.println("target:"+target+"mindistance:"+mindistance);
	  // bw.write("target:"+target+"mindistance:"+mindistance);
	   if((requester==-1||requester!=target)&&target!=-1)
	    {//if3
		   int res=findgroup(target,turn,index);
		   if(res==index) {//if31
			   files[index].group=files[index].group!=-1?files[index].group:ngroup++;
			   files[target].group=files[index].group;
			   groups--;
			   files[index].isleader=1;
			   files[target].isleader=0;
			   for(int j=0;j<files[target].member_num;j++)
			    {//for1
				   files[index].members[files[index].member_num++]=files[target].members[j];
				   files[files[target].members[j]].isleader=0;
				   files[files[target].members[j]].group=files[index].group;
			    }//for1
		   }//if31
		   return -1;
	    }else if((requester!=-1)&&(requester==target)&&target!=-1) {//if3 if5
	    	return target;
	      }else{//if5 if6
	    	return -1;  
	      }//if6
    }//findgroup
   public static void _2_2closego() throws IOException
   {//2_2close
	   int turn=1;
	   for(int i=0;i<files.length;i++)
	    {//for1
		   File file=new File(max_txt,i);
		   files[i]=file;
	    }//for1
	   while(groups>thres) 
	    {//wh03
	      for(int i=0;i<files.length;i++)
	       {//for1
	    	  System.out.println(i);
	    	  findgroup(i,turn,-1); 	   
	       }//for1
	      try {
			printout(turn);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	      turn++;
	    }//wh03
   }//2_2close
   public static void printout(int turn) throws IOException
   {//print_out
	   String output="D:\\InformationTheoryGroupHomeWork\\ans2.txt";
	   FileOutputStream out=new FileOutputStream(output);
	   OutputStreamWriter fs=new OutputStreamWriter(out);
	   BufferedWriter bw=new BufferedWriter(fs);
	   int group=0;
	   String anstr="";
	   for(int i=0;i<files.length;i++)
	    {//for1
		   if(files[i].group==-1) {group++;}
		   if(files[i].group!=-1&&files[i].isleader==1) 
		   {//if1
			   group++;
		       anstr+="第"+files[i].group+"组共:"+files[i].member_num+"个元素\n";
		       String members="";
		       for(int j=0;j<files[i].member_num;j++)
		        {
		    	   members+=files[i].members[j]+",";
		    	   //System.out.println(files[i].members[j]);
		        }
		       System.out.println("成员"+members);
		   }//if1
	    }//for1
	   System.out.println("第"+turn+"轮共:"+group+"个类别");
	   System.out.println(anstr);
	   bw.write(anstr);
	   bw.close();
	   fs.close();
   }//print_out
  public static void generate_distance(String filename,int sheet) throws IOException 
  {//gd
	   for(int i=0;i<files.length;i++)
	    {//for1
		   File file=new File(max_txt,i);
		   files[i]=file;
	    }//for1
	    HSSFWorkbook wbfile=new HSSFWorkbook();
	   HSSFSheet sheeter=wbfile.createSheet("0");
	  for(int i=0;i<max_txt;i++) 
	   {//for1
		  String anstr="";
		  System.out.println("计算第"+i+"个点");
		  for(int j=0;j<max_txt;j++) 
		   {//for2
			  double distance = calculate_distance(i,j);
			  if(j<max_txt-1) {
				  anstr+=distance+",";
			  }else {
				  anstr+=distance+"";
			  }
		   }//for2
		  HSSFRow row = sheeter.createRow(i);
		  HSSFCell cell = row.createCell(0);
		  cell.setCellValue(anstr);
		  System.out.println("完成第"+i+"个点的计算");
	   }//for1
	   FileOutputStream out=new FileOutputStream(filename);
	   wbfile.write(out);
	   out.close();
  }//gd
  static double get_distance(int a,double array[])
   {//get_d
	  double ans = 0;
	  for(int i=0;i<files[a].member_num;i++)
	   {//for 1
		  ans+=array[files[a].members[i]];
	   }//for 1
	  ans/=files[a].member_num;
	  return ans;
   }//get_d
  static double[] get_array(int index) throws IOException 
   {//ga
	  InputStream inputstream=new FileInputStream("D:\\InformationTheoryGroupHomeWork\\distance.xls");
  	  HSSFWorkbook wb=new HSSFWorkbook(inputstream);
  	  HSSFSheet sheeter=wb.getSheetAt(0); 
	  double array[]=new double[max_txt];
	  for(int i=0;i<files[index].member_num;i++)
	   {//for1
		  HSSFRow row=sheeter.getRow(files[index].members[i]);
		  HSSFCell cell = row.getCell(0);
		  String str = cell.getStringCellValue();
		  String array_str[]=str.split(",");
		  for(int j=0;j<array_str.length;j++) 
		   {//for2
			  array[j]+=Double.parseDouble(array_str[j])/files[index].member_num;
		   }//for2
	   }//for1
	  return array;
   }//ga
}
