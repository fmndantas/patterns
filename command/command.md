# Command pattern

An object is used to encapsulate all the information needed to perform
action or trigger an event at later time. 

An example is an installation wizard. The user goes through the wizard
setting his/her preferences. 

The preferences are stored in `Command` object. When the wizard is done,
the `Command.execute()` is ran and the installation is proceeded.

The `Command` object, thus, stores all the information to trigger 
an installation.

Another examples are:

* Encapsulating an request as an object
* Allowing the parametrization of clients with different requests
* Allowing to save the requests in an queue

There are four main roles in the command pattern:
* Command
* Receiver
* Invoker
* Client

1. The (concrete) `Command` knows the `Receiver` and execute its method
2. Values for `Receiver` method are stored in the `Command`
3. The `Invoker` knows how to execute a `Command`
4. The `Client` creates a `Command` and set its `Receiver`