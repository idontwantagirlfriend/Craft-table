import scrapy
import os

# readme
# 5 steps to follow:
# Firstly, specify the spider parameters. Check the path for the website objects and see if they can still match the information you want to collect. Change your start_urls and the nextpage variable (which points to the next page to crawl after self.parse() has been run for a time) to the first page on the index page like "...?page=1..." specifically for the website you want to crawl
# Secondly, check if you are already having some old results crawled in the working directory. If yes, modify the resulting file names (stored in "name") either with naming paradigm (like "STFRFRNS$$$$") or the offset counter (confer the code)
# Thirdly, check the index limit. Basically until which page you want to stop collecting. This is used for only collecting data before a time limit, for example when you only want articles before the year 2020, or after this june. 
# Fourthly, test the code. don't forget to comment the part that overwrites the crawled text files.
# Finally, uncomment the overwrite part and get the results. 


class spider1(scrapy.Spider):

# Spider parameter: URL
    name="watson"
    start_urls=["https://www.rtbf.be/culture/archive_scene?page=1&dossier=2433"]

    def __init__(self):
        name="watson"

# Spider parameter: URL
    # Musique
        # start_urls=["https://www.rtbf.be/culture/archive_musique?page=1&dossier=2443"]
    # Cinéma
        # start_urls=["https://www.rtbf.be/culture/archive_cinema?page=1&dossier=2393"]
    # Scène
        start_urls=["https://www.rtbf.be/culture/archive_scene?page=1&dossier=2433"]

        index=0
    # The last counter in the gathered results
        counter=211

        self.name=name
        self.start_urls=start_urls

        self.index=index
        self.counter=counter

        # Section Time only in rtbf part
        self.section_time=""

        # self.ChinaList=[]
        # self.InternationalList=[]

    def crawltext(self, response):
        # self.log(dir(response))
        # if bool(response.xpath("//*[@class='clearfix text-formatted field field--name-field-corps-de-texte field--type-text-long field--label-hidden field__item']//descendant-or-self::text() | //div[@class='paragraph paragraph--type--paragraphe paragraph--view-mode--default']/h2//text()").get())==False:
        #     return
        
        temp_txt=" ".join(response.xpath("//div[@itemprop='articleBody' and contains(@class,'rtbf-article')]//descendant::p[not(@data-favorite_site)]//text()").getall())
        title=response.xpath("//h1//text()").get()
        title=title.strip()
        time=self.section_time

        self.counter+=1
        name="STFRBENS07{:0>4}.txt".format(self.counter)

        # Detector of void data 
        if bool(time)==False:
            self.log("Void time found on {}".format(name))
        if bool(title)==False:
            self.log("Void title found on {}".format(name))
        if bool(temp_txt)==False:
            self.log("Void content found on {}")

        # for i in ["China","china","Chinese","chinese","PRC","Taïwan","taïwan","Taiwan","taiwan","Chine","chine","Chinoi", "chinoi"]:
        #     if (i in temp_txt) or (i in title):
        #         self.log("{} is China related and International.".format(name))
        #         if name in self.ChinaList:
        #             pass
        #         else:
        #             self.ChinaList.append(name)
        #     for i in ["UE","europ","Europ","d Bretagn","Russ","russe","Asie","asie","siatique","fricain","Afrique"," belg","llema","Ital","italie","espagn","austral","Berli","London","ingapo"]:
        #         if (i in temp_txt) or (i in title):
        #             self.log("{} is International.".format(name))
        #             if name in self.InternationalList:
        #                 pass
        #             else:                    
        #                 self.InternationalList.append(name)

        # ChinaHHH=""
        # for i in self.ChinaList:
        #     ChinaHHH+="{}, ".format(i)
        # InternationalHHH=""
        # for i in self.InternationalList:
        #     InternationalHHH+="{}, ".format(i)
        # self.log("By now all the china related and international: {}\n all the international: {}".format(ChinaHHH,InternationalHHH))

        # # Write the files
        thispath=os.path.join(os.getcwd(),"A7",name)
        csvpath=os.path.join(os.getcwd(),"A7","metadata.csv")

        # Metadata items
        Updater="丁宇"
        File="法语，比利时，新闻报道，娱乐，{:0>4}".format(self.counter)
        Filename="STFRBENS07{:0>4}".format(self.counter)
        Nationality="Belgium"
        Language="French"
        Category="entertainment"
        Area="domestic"
        ChinaRelated="no"
        Source="rtbf culture"
        Date=time
        Reporter="N/A"
        Title=title
        _url=response._url
        STIT="individual text"
        AlignmentFile="N/A"

        with open(thispath,mode="a",encoding="utf-8") as file:
            file.write(title)
            file.write("\n")
            file.write(temp_txt)
        with open(csvpath,mode="a",encoding="utf-8") as csv:
            csv.write("{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}	{}\n".format(Updater,File,Filename,Nationality,Language,Category,Area,ChinaRelated,Source,Date,Reporter,Title,_url,STIT,AlignmentFile))
        # yield {
        #     "url":response,
        #     "title":title,
        #     "time":time,
        #     "text":temp_txt
        # }
        # yield {
        #     "###":"###"+str(response)
        # }
# cssselect.response has the following attributes: 
# __bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_css2xpath', '_csstranslator', '_default_namespaces', '_default_type', '_expr', '_get_root', '_lxml_smart_strings', '_parser', '_tostring_method', 'attrib', 'css', 'extract', 'get', 'getall', 'namespaces', 're', 're_first', 'register_namespace', 'remove', 'remove_namespaces', 'response', 'root', 'selectorlist_cls', 'text', 'type', 'xpath'
 
#  From Vie publique
    # def parse(self, response):
    #     for link in response.css(".link-multiple"):
    #         yield scrapy.Request("https://www.vie-publique.fr"+link.attrib["href"], callback=self.crawltext)
    #     if self.index<18:
    #         self.index+=1
    #         nextindex="https://www.vie-publique.fr/justice-droits-fondamentaux?page={}".format(self.index)
    #         yield scrapy.Request(nextindex, callback=self.parse)

# From rtbf spider
    def parse(self, response):
        for section in response.css('.rtbf-article-grid.rtbf-archive__section'):
            self.section_time=french_time(section.xpath("//time[contains(@class,'www-time--title')]//text()").get())
            
            for item in section.xpath('//article[contains(@class, "rtbf-article-grid__item")]//a[not(@class)]//attribute::href'):
                # Old
                # yield {
                #     "title":item.get(),
                #     "date":section_time
                # }
                yield scrapy.Request(item.get(), callback=self.crawltext)

        # Old
        # nextpage=response.css('a[aria-label="Page suivante"]::attr(href)').get()
        # if nextpage is not None:
        #     nextpage="{}{}".format("https://www.rtbf.be/info/archive_monde",nextpage)
        #     yield scrapy.Request(nextpage, callback=self.parse)

        if self.index<3:
            self.index+=1

    # For different themes:
        # Musique:
            # nextindex="https://www.rtbf.be/culture/archive_musique?page={}&dossier=2443".format(self.index)
        # Cinéma:
            # nextindex="https://www.rtbf.be/culture/archive_cinema?page={}&dossier=2393".format(self.index)
        # Scène:
            nextindex="https://www.rtbf.be/culture/archive_scene?page={}&dossier=2433".format(self.index)
            yield scrapy.Request(nextindex, callback=self.parse)

# class spider2E(scrapy.Spider):
#     def __init__(self):
#         name="emma"
#         start_urls="https://www.rtbf.be/culture/archive_cinema?page=1&  dossier=2393"
#         index="0"
#         self.name=name
#         self.start_urls=start_urls
#         self.index=index
    
#     def parse(self,response):
        
def french_time(stringing):
    stringing=stringing.strip()
    stringing.lower()
    if stringing[-4:].isdigit():
        year=stringing[-4:]
        if stringing[:2].isdigit():
            day=stringing[:2]
            if "jan" in stringing:
                month="01"
            elif "fev" in stringing or "fév" in stringing:
                month="01"
            elif "mar" in stringing:
                month="01"
            elif "avr" in stringing:
                month="01"
            elif "mai" in stringing:
                month="01"
            elif "juin" in stringing:
                month="01"
            elif "jui" in stringing:
                month="01"
            elif "aou" in stringing or "aoû" in stringing :
                month="01"
            elif "sep" in stringing:
                month="01"
            elif "oct" in stringing:
                month="01"
            elif "nov" in stringing:
                month="01"
            elif "dec" in stringing or "déc" in stringing :
                month="12"
            else:
                return
        else:
            return
    else:
        return

    return "{}-{}-{}".format(year,month,day)
