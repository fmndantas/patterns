# Façade pattern

## Goal 

* When people walk past a façade, they can
appreciate the exterior face but aren't aware of the complexities of the structure
within. This is how a façade pattern is used.

* Façade hides the complexities of the
internal system and provides an interface to the client that can access the system in a
very simplified way.

* Consider the example of a storekeeper. Now, when you, as a customer, visit a
store to buy certain items, you're not aware of the layout of the store. You typically
approach the storekeeper, who is well aware of the store system. Based on your
requirements, the storekeeper picks up items and hands them over to you. Isn't this
easy? The customer need not know how the store looks and s/he gets the stuff done
through a simple interface, the storekeeper.

The Façade design pattern essentially does the following:

1. It provides a unified interface to a set of interfaces in a subsystem and defines
a high-level interface that helps the client use the subsystem in an easy way

2. Façade discusses representing a complex subsystem with a single interface
object. It doesn't encapsulate the subsystem but actually combines the
underlying subsystems.

3. It promotes the decoupling of the implementation with multiple clients.

## Structure

### Façade
* An interface that knows which type of request should be addressed to each one of the subsystems
* Delegates the client's request to the right subsystem through composition

### System
* Handles the requests made by the Façade, but has not knowledge of the façade
* It is composed by a set of subsystems (classes), that implements different operations.

### Client
* _Instantiate_ the façade
* It makes requests to the façade, that make requests to the system.

## Principle of least knowledge

* The classes should be decoupled to each other
* The interaction between objects from different classes should happen through a few _friends_ that are
close enough to the _client_.
* Coupling between classes often leads to the software regression.