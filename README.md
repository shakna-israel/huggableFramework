# Huggable Framework

[Hug](https://github.com/timothycrosley/hug) is an exciting API framework with built in versioning, and many content types.

Its powerful, robust, and built on Falcon.

That being said - it can be easily abused, and produce a powerful web framework.

The file [demo.py](demo.py) demonstrates exactly how easy it is to produce HTML.

## Issues with Demonstration

* The templating engine was taken from Bottle. If you have Bottle, you may as well use it.
    * Other templating engines are often standalone, and could be exploited in a similar way.
* As Hug is designed to host APIs, and the underlying backbone, Falcon, is also designed to host APIs, there may be some issues with rendering large amounts of requests.
* Hug is far from asynchronous, which may mean flooding it with requests could kill it easily.

## Affiliation Statement

I am in no way affiliated with Hug or Falcon.

I just saw an opportunity and took it.

## License

Released to the public domain.

See [LICENSE](LICENSE.md) for more.
