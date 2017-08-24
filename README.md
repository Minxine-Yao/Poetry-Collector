# Poetry Collector

## Introduction

An application that collect old Chinese poems into a Markdown file with the input of catalog file,all the poems are scraped from the [古诗文网](http://www.gushiwen.org/).For some unknown reasons, the comments of some poems cannot be scraped normally, which I know currently is listed below:

* 《山居秋暝》王维

## How to use

```
py poetry_collector.py catalog_filepath
```

## The Structure of Catalog

Catalog is a txt file with the coding format ANSI, the structure of it was described below.

> [ Anything without '…' ]
>
> **Author**
>
> **Title…(any more)…Page number**
>
> [ Anything without '…' or any more structure like what I've written above ]
>
> **Author**
>
> **Title(partial)**
>
> **[ Any more partial title ]**
>
> **Title(partial)…(any more)…Page number**
>
> [ Anything without '…' or any more structure like what I've written above ]

* example:

> 王安石
>
> 元日……………………………………………………………………………220
>
> 明妃曲(其一)…………………………………………………………………221
>
> 明妃曲（其二）………………………………………………………………222
>
> 苏 轼
>
> 惠崇春江晚景二首……………………………………………………………223
>
> 惠州一绝………………………………………………………………………224
>
> 世传徐凝《瀑布》诗云：一条界破青山色。至为尘陋。
>
> 又伪作乐天诗称美此句，有“赛不得”之语。
>
> 乐天虽涉浅易，然岂至是哉！乃戏作一绝…………………………………225

