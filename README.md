# hermes_cli
A tracking info for Hermes postal service

## Usage (CLI)

    hermes_cli $THE_ID
### CLI options
      --zusammenfassung, -z          Only show a summary of the returned info
## Usage (external scripts)
        from hermes_cli import getTrackInfo
        tracking = getTrackInfo('$THE_ID')

This is some sample data the tool will return...       

        {
          "shipmentID" : "02336117005705",
          "statusImageID" : 5,
          "lastStatus" : {
            "description" : "Die Sendung wurde zugestellt. ",
            "dateTime" : "05.12.2018 15:29"
          },
          "statusHistory" : [ {
            "description" : "Die Sendung wurde zugestellt. ",
            "dateTime" : "05.12.2018 15:29"
          }, {
            "description" : "Die Sendung befindet sich in der Zustellung.",
            "dateTime" : "05.12.2018 08:01"
          }, {
            "description" : "Die Sendung ist im Hermes Verteilzentrum Berlin-Vogelsdorf eingetroffen. ",
            "dateTime" : "04.12.2018 23:27"
          }, {
            "description" : "Die Sendung wurde im Hermes Logistikzentrum sortiert.",
            "dateTime" : "04.12.2018 10:00"
          }, {
            "description" : "Die Sendung wurde im Hermes Verteilzentrum Essen sortiert.",
            "dateTime" : "03.12.2018 19:30"
          }, {
            "description" : "Die Sendung befindet sich im Hermes Verteilzentrum Essen.",
            "dateTime" : "03.12.2018 19:30"
          }, {
            "description" : "Die Sendung wurde im Hermes PaketShop abgeholt und für den weiteren Transport sortiert.",
            "dateTime" : "03.12.2018 14:03"
          }, {
            "description" : "Die Sendung ist im Hermes PaketShop eingegangen.",
            "dateTime" : "03.12.2018 11:37"
          }, {
            "description" : "Die Sendung wurde Hermes elektronisch angekündigt.",
            "dateTime" : "02.12.2018 18:32"
          } ],
          "city" : null,
          "countryCode" : "DEU",
          "zipCode" : null,
          "expectedDate" : "05.12.2018",
          "expectedTimeEarliest" : null,
          "expectedTimeLatest" : null
        }
