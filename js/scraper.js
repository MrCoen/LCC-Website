const cheerio = require('cheerio');
const puppeteer = require('puppeteer');

 

let scraped_headlines= [];

 

(async()=>{
  const browser=await puppeteer.launch();
  const page=await browser.newPage();

 

    try{</span
      await page.goto('https://www.reddit.com/r/webscraping/', {timeout: 180000});
      let bodyHTML=await page.evaluate(()=> document.body.innerHTML);
      let $=cheerio.load(bodyHTML);
      let article_headlines=$('a[href*="/r/webscraping/comments"] > div')
      article_headlines.each((index,element)=>{
          title=$(element).find('h3').text()
          scraped_headlines.push({
            'title': title
          })
      });

 

      } catch(err) {
          console.log(err);
      }

 

      await browser.close();
    console.log(scraped_headlines)
})();