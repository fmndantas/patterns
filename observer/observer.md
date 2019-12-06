# Observer pattern

* Subject
    * The entity that will be observed

* Observers
    * List of entities maintained by the subject. 
    * Each one of the observers will be notified when
    the subject has changed. 
    * The notification will happen through some method 
    defined by the subject.
    
* Observer pattern methods
    * Pull
        * The subject notifies all observers that there is a change
        * The observers are **responsible** for getting the changes
        * This methods is relatively ineffective as it involves the 
        two mentioned steps
    * Push
        * The subject pushes the changes to the observers
        * The subject may send too much detailed information
        to the observers, which results in slower execution
        and performance.
        * Ideally, only the **needed information** should be sent to
        the observer.