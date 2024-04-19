## Chal 1:  
  $ sudo gunzip /usr/share/wordlists/rockyou.txt.gz  
  $ john --wordlist=/usr/share/wordlists/rockyou.txt weregonnarock.txt  

## Chal 3:  
Get hashcat scrapers: https://github.com/stricture/hashstack-server-plugin-hashcat/blob/master/scrapers/office2hashcat.py  
python3 office2hashcat.py TOP_SECRET_PRESENTATION.pptx > officehash.txt  
hashcat officehash.txt rockyou.txt  
Pass: dieold718  

## Chal 4:  
Download ophcrack  
Load in XP free fast table  
Load in hash  
Hit crack  
Pass: 1LUCKYS  
 
