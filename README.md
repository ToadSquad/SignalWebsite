# SignalWebsite
Premium Signals Delivered to You!

## Built With Django


### Homepage
![Image](https://i.imgur.com/K3h7WCq.png)

### /signalsob
![Image](https://i.imgur.com/rivLB0L.png)


# How to run

## Requirements

```
pip install -r requirements.txt
```
## Running the server
```
python manage.py makemigrations
python manage.py runserver
```

# Project Aspects

## cryptoOrderBookScanner.py
```
self.scanner = BinanceScanner(5,2)
```
The crypto orderbook scanner takes an input parameter of diff and ratio the diff is depth amount the scanner will look into the orderbook in percent, the ratio is the buy/sell volume ratio in which triggers are added to the list
self.obTriggerList = {}

* 18943 * 1.05 = 19,890.15 Upper Bound
* 18943 * .95 = 17,995.85  Lower Bound

Drawn out is the area in which the scanner will add up the order totals and take the differential

![image](https://user-images.githubusercontent.com/36092187/192161196-c7599d66-46b4-4f15-9f22-9360f5013918.png)
![image](https://i.imgur.com/DbzGACg.png)
![image](https://i.imgur.com/1wOVLL3.png)


## Sqllite Database
Django is configured to use the default sqllite database for our purposes this is fine.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```


### Models.py
triggerData defines the fields in which active trades are taken these are the trades that get triggered from the cryptoOrderBookScanner.py
```
class triggerData(models.Model):
    symbol = models.CharField(max_length=30)
    direction = models.CharField(max_length=30)
    ratio = models.CharField(max_length=30)
    upper = models.CharField(max_length=30)
    lower = models.CharField(max_length=30)
    time = models.DateTimeField()
    priceEntered = models.CharField(max_length=30)
    currentPL = models.CharField(max_length=30)
    profit = models.CharField(max_length=30)
```

## Project Flow
In the __init__.py file multithreading is ulilized to run the scriptmanager.py file which is set to run every 15 minutes.

## Views
The /signalob page builds a table utilizes Djangos built in functionality with context
```
{% for trigger in triggers %}
            <tr>
            <td>{{trigger.symbol}} </td>
            <td class={{trigger.direction}}>{{trigger.direction}}</td>
            <td>{{trigger.ratio}}</td>
            <td>{{trigger.upper}}</td>
            <td>{{trigger.lower}}</td>
            <td class="time">{{trigger.time}}</td>
            <td>{{trigger.profit}}</td>
            <td class="PL">{{trigger.currentPL}}</td>
            <td class={{trigger.priceEntered}}>{{trigger.priceEntered}}</td>
            </tr>
            {% endfor %}
```
```
def signalsob(request):
    global obdata
    context = {}
    #file = open("triggers.dat", "rb")
    #context = pickle.load(file)
    data = {}
    historyData = triggerData.objects.all().exclude(priceEntered="entered")
    totalProfit = 0
    winCount = 0
    if(len(historyData)>0):
        for trigger in historyData:
            totalProfit += float(trigger.currentPL)
            if(trigger.priceEntered == "profit"):
                winCount += 1
        context['totalProfit'] = totalProfit
        context['accuracy'] = winCount/len(historyData)

    if(request.method == 'POST'):
        context['triggers'] = historyData
        
    else:
        context['triggers'] = triggerData.objects.all().filter(priceEntered="entered")
        totalProfit = 0
        for trigger in context['triggers']:
            totalProfit += float(trigger.currentPL)
        context['urealized'] = totalProfit    
    #get data from database
    print(context)
    #file.close()
    
    return render(request,'signalpage.html',context)
```


