package main;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;

public class generate_words {
    static int max_txt=398;
    static Map<String,Integer> words;
    
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
       words=new HashMap<String,Integer>();
       String filename="D:\\InformationTheoryGroupHomeWork\\14AAAI.xls";
       String outfile="D:\\InformationTheoryGroupHomeWork\\words.xls";
       int sheet=0;
       count_words(filename,sheet);
       savetofile(outfile,sheet);  
       System.out.println("写入完成！");
	}
	public static void count_words(String filename,int sheet) throws IOException
	{//ct
	 	InputStream inputstream=new FileInputStream(filename);
    	HSSFWorkbook wb=new HSSFWorkbook(inputstream);
    	HSSFSheet sheeter=wb.getSheetAt(sheet);
		for(int i=1;i<max_txt+1;i++) 
		 {//for1
			System.out.println("开始第"+i+"轮写入");
			HSSFRow row = sheeter.getRow(i);
			int cols[]= {0,3,5};
			String str="";
			  for(int j=0;j<cols.length;j++)
			   {//for2
				  HSSFCell cell = row.getCell(cols[j]);
				  str+=cell.getStringCellValue()+" ";
			   }//for2
			  System.out.println(str);
			  handle(str);
			  System.out.println("第"+i+"轮完成");
		 }//for1
	}//ct
	public static void handle(	String str) 
	{//handle
		String str_array[]=str.split(" ");
		System.out.println(str_array.length);
		Map<String,Integer> map=new HashMap<String,Integer>();
		 for(int i=0;i<str_array.length;i++)
		  {//for1
			 map.put(str_array[i],1);
		  }//for1
		 Set<String> key=map.keySet();
		 java.util.Iterator<String> it=key.iterator();
		 while(it.hasNext())
		 {//wh09
			 String word=it.next();
			 if(words.containsKey(word)){//if2				 
				 int on=words.get(word);
				 words.put(word,on+1);
			 }else{//if2
				 words.put(word,1);
			 }
		 }//wh09
	}//handle
   public static void savetofile(String filename,int sheet) throws IOException
    {//savetofile
	    HSSFWorkbook book=new HSSFWorkbook();
	    HSSFSheet sheeter=book.createSheet("关键词");
	    Set<String> key=words.keySet();
	    java.util.Iterator<String> it=key.iterator();
	    int i=0;
	    while(it.hasNext())
	     {//wh1
	    	HSSFRow row=sheeter.createRow(i);
	    	HSSFCell cell_word=row.createCell(0);
	    	HSSFCell cell_freq=row.createCell(1);
	    	String word=it.next();
	    	cell_word.setCellValue(word);
	    	cell_freq.setCellValue(words.get(word));
	    	i++;
	     }//wh1
	    FileOutputStream out=new FileOutputStream(filename);
		   book.write(out);
    }//savetofile
}
