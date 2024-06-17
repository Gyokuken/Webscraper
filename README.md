To do the title scraping, of 10 videos (can be changed in the code) Three libraries have been used
1. Time
2. selenium -> webdriver :  A WebDriver is a browser automation framework. It accepts commands and sends them to a browser.
3. BeautifulSoup : Used to parse the html content and find the video titles and timestamps

The output generated is the Title : {Title of the video}, Timestamp: {timestamp}
In the background, it uses integration of a specific delegate in TensorFlow Lite (TFLite) to optimize performance on CPU-based devices. TFlite specifically which is just a lighter version of tensorflow.
