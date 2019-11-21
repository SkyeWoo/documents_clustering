package main;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;

public class tfdt {
    static int max_txt=398;
    static HSSFSheet Rsheeter,wrsheeter,wsheeter;
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		String txt_file="D:\\InformationTheoryGroupHomeWork\\14AAAI.xls";
		String word_file="D:\\InformationTheoryGroupHomeWork\\words.xls";
		InputStream inputstream=new FileInputStream(txt_file);
    	HSSFWorkbook wb=new HSSFWorkbook(inputstream);
    	 Rsheeter=wb.getSheetAt(0);
    	 InputStream inputstream2=new FileInputStream(word_file);
     	 HSSFWorkbook wb2=new HSSFWorkbook(inputstream2);
     	 wrsheeter=wb2.getSheetAt(0); 
     	read_word();
	}
    public static void read_word() throws IOException 
    {//read_word
    	HSSFWorkbook wbook=new HSSFWorkbook();
    	HSSFSheet wsheeter=wbook.createSheet("0");
    	FileOutputStream out=new FileOutputStream("D:\\InformationTheoryGroupHomeWork\\tfdt.xls");
       for(int i=1;i<max_txt+1;i++) 
        {//for1
    	   System.out.println("第"+i+"个论文读取");
    	   HSSFRow row=Rsheeter.getRow(i);
    	   int cols[]= {0,3,5};
    	   String str="";
    	   int n=0;
    	   for(int j=0;j<cols.length;j++) 
    	     {//for12
    		   HSSFCell cell=row.getCell(cols[j]);
    		   str+=cell.getStringCellValue()+" ";
    	     }//for12
    	   //System.out.println(str);
    	   //System.out.println(wrsheeter.getLastRowNum());
    	   String anstr="";
    	   for(int k=0;k<wrsheeter.getLastRowNum();k++)
    	     {//for13
    		  //System.out.println(k);
    		   HSSFRow rwrow=wrsheeter.getRow(k);
    		   String word=rwrow.getCell(0).getStringCellValue();
    		   //System.out.println(word);
    		   int count=count_in(str,word);
    		   if(k<wrsheeter.getLastRowNum()-1) {
    		   anstr+=count+",";
    		   }else {
    		   anstr+=count+"";	   
    		   }
    	     }//for13   
    	   HSSFRow wrow=wsheeter.createRow(i-1);
    	   HSSFCell cell=wrow.createCell(0);
    	   cell.setCellValue(anstr);
    	   System.out.println("第"+i+"个文件读取完成");
        }//for1	
       wbook.write(out);
	   System.out.println("读写完成");
    }//read_word
    public static int count_in(String str,String word) 
     {//count_in
    	int index = str.indexOf(word,0),num=0;
    	if(index>=0)num++;
    	while(index>=0&&index+word.length()<str.length()) 
    	 {//wh01
    		index=str.indexOf(word,index+word.length());
            num++;
    	 }//wh01
    	return num;
     }//count_in
}
