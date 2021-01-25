package com.hankcs.hanlp;

import com.hankcs.hanlp.classification.classifiers.IClassifier;
import com.hankcs.hanlp.classification.classifiers.NaiveBayesClassifier;
import com.hankcs.hanlp.classification.corpus.IDataSet;
import com.hankcs.hanlp.summary.TextRankKeyword;

import java.awt.*;
import java.io.*;
import java.util.List;

public class extract {
    //C:\Users\LYL\Desktop\hanlp\HanLP-1.x\data\test\ChnSentiCorp情感分析酒店评论
    String Training_data_address="C:\\Users\\LYL\\Desktop\\train";
    public static void main(String args[])throws IOException{
        extract extract=new extract();
        //extract.SentimentAnalysis();
        //extract.get_key_words();
        //extract.get_likes();
        //extract.get_comments();
        extract.SentimentAnalysis();

    }
    public void get_key_words()throws IOException{
        //document=content=文本内容
        String key_words_destination="C:\\Users\\LYL\\Desktop\\txt\\keywords_of_comments_only\\";
        String source_info="C:\\Users\\LYL\\Desktop\\txt\\comments_only\\";
        int count=1;
        while (count<11972){
            File source_file=new File(source_info+name(count));
            File dest_file=new File(key_words_destination+name(count));
            BufferedReader reader=new BufferedReader(new InputStreamReader(new FileInputStream(source_file),"UTF-8"));
            OutputStreamWriter writer=new OutputStreamWriter(new FileOutputStream(dest_file),"UTF-8");
            String a="";
            String b="";
            while((b=reader.readLine())!=null){
                a=a+b;
            }
            List<String> keywords=TextRankKeyword.getKeywordList(a,15);
            int i=0;
            for(i=0;i<keywords.size();i++){
                writer.append(keywords.get(i)+" ");
            }
            writer.close();
            reader.close();
            count++;
        }

    }
    public String name(int count){
        String cnt=String.valueOf(count);
        while(cnt.length()<6){
            cnt="0"+cnt;
        }
        return cnt+".txt";
    }

    public void get_likes()throws IOException{
        //document=content=文本内容
        String dest="C:\\Users\\LYL\\Desktop\\toutiao\\likes&comments\\likes.txt";
        String source_info="C:\\Users\\LYL\\Desktop\\toutiao\\split\\";
        File dest_file=new File(dest);
        OutputStreamWriter writer=new OutputStreamWriter(new FileOutputStream(dest_file),"UTF-8");

        int count=1;
        while (count<14618){
            File source_file=new File(source_info+name(count));
            BufferedReader reader=new BufferedReader(new InputStreamReader(new FileInputStream(source_file),"UTF-8"));
            reader.readLine();
            reader.readLine();
            reader.readLine();
            String a=reader.readLine().substring(12);
            a=a.substring(0,a.length()-1);
            //System.out.println(a);
            writer.append(a+"\n");
            reader.close();
            count++;
        }
        writer.close();

    }
    public void get_comments()throws IOException{
        //document=content=文本内容
        String dest="C:\\Users\\LYL\\Desktop\\toutiao\\likes&comments\\comments.txt";
        String source_info="C:\\Users\\LYL\\Desktop\\toutiao\\split\\";
        File dest_file=new File(dest);
        OutputStreamWriter writer=new OutputStreamWriter(new FileOutputStream(dest_file),"UTF-8");

        int count=1;
        while (count<14618){
            File source_file=new File(source_info+name(count));
            BufferedReader reader=new BufferedReader(new InputStreamReader(new FileInputStream(source_file),"UTF-8"));
            reader.readLine();
            reader.readLine();
            reader.readLine();
            reader.readLine();
            String a=reader.readLine().substring(11);
            a=a.substring(0,a.length()-1);
            //System.out.println(a);
            writer.append(a+"\n");
            reader.close();
            count++;
        }
        writer.close();

    }


    public void SentimentAnalysis() throws IOException{
        IClassifier classifier = new NaiveBayesClassifier(); // 创建分类器，更高级的功能请参考IClassifier的接口定义
        classifier.train(Training_data_address);                     // 训练后的模型支持持久化，下次就不必训练了
        //split_sort(classifier,"C:\\Users\\LYL\\Desktop\\to be trained\\renmin\\",11972);
        //split_sort(classifier,"C:\\Users\\LYL\\Desktop\\to be trained\\toutiao\\",14618);
        split_sort(classifier,"C:\\Users\\LYL\\Desktop\\to be trained\\zhongguoxinwen\\",8092);
    }

    public void split_sort(IClassifier classifier, String addr,int a) throws IOException {
        int count=1;
        while (count<a){
            File source=new File(addr+name(count));
            BufferedReader reader=new BufferedReader(new InputStreamReader(new FileInputStream(source),"UTF-8"));
            String info=reader.readLine();
            String folder=predict(classifier,info);
            File dest=new File("C:\\Users\\LYL\\Desktop\\sorted\\"+folder+"\\中国新闻网\\"+name(count));
            OutputStreamWriter writer=new OutputStreamWriter(new FileOutputStream(dest),"UTF-8");
            writer.append(info);
            writer.close();
            reader.close();
            count++;
            //File dest=new File("C:\\Users\\LYL\\Desktop\\sorted")
        }

    }
    public String predict(IClassifier classifier, String text){
        //System.out.printf("《%s》 情感极性是 【%s】\n", text, classifier.classify(text));
        return classifier.classify(text);
    }
    {
        File corpusFolder = new File(Training_data_address);
        if (!corpusFolder.exists() || !corpusFolder.isDirectory())
        {
            System.err.println("没有文本分类语料，请阅读IClassifier.train(java.lang.String)中定义的语料格式、准备语料");
            System.exit(1);
        }
    }




}
