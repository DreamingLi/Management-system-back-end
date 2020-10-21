# Management-system-back-end

该项目使用了Django3 的ASGI异步框架，性能相对于同步的WSGI大约提升3-5倍。
这个项目有web chat的需求，因此使用了channel库来支持。项目前端是react框架，正常来说，socket.io是首选，但是由于Django并没有支持seocket.io，因此 使用了channel （websocket）来代替。

目前整个项目还在开发中，聊天功能基本完成，只差表情等小功能需要实现。另外对于任务的分发，接收，交付还没有完成。


This project uses the ASGI asynchronous framework of Django3, and its performance is about 3-5 times higher than WSGI.
Channel is used in this project to support webchat, The front end of this project is the React framework. Since Django does not support seocket.io, channel (websocket) 
is used instead. 

This project is still on developing, the function of web chat is almost completed, but such as emoji function is not completed.
