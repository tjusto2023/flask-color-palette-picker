from kink import di as container
from typing import TypeVar, Type, Callable

T = TypeVar('T')
U = TypeVar('U')

class DependencyInjection():

    __register_request = {}

    @staticmethod
    def _checkClass(instance_class: Type[U], interface: Type[T]) -> None:
        """
        Checks if the given class is a subclass of the specified interface.

        Args:
            instance_class (Type[U]): The class to check.
            interface (Type[T]): The interface that the class is expected to subclass.

        Raises:
            TypeError: If the class is not a subclass of the interface.
        """
        if not issubclass(instance_class, interface):
            raise TypeError(f"The class must be a subclass of {interface.__name__}")
    
    @staticmethod
    def startRequest() -> None:
        for key, value in DependencyInjection.__register_request.items():
            container.factories[key] = lambda c: value()
            container.factories[key.__name__] = lambda c: value()

    @staticmethod
    def endRequest() -> None:
        for key in DependencyInjection.__register_request:
            del container.factories[key]
        
        container.clear_cache()

    @staticmethod
    def inject(interface: Type[T]):
        """
        Inject the service, allowing a request container to be passed in.
        This simulates the scoped behavior where instances are retained within a request.
        """

        if interface not in container:
            raise ValueError(f"{interface.__name__} was not registered.")
        
        return container[interface]

    @staticmethod
    def addSingleton(interface: Type[T], instance_class: Callable[[], U]) -> None:
        """
        Registers a service with a singleton lifetime.

        Singleton: Use when you need to reuse a service across multiple points in your application, 
        such as application configurations, parameters, logging services, or data caching.
        
        Args:
            interface (Type[T]): The interface type to register.
            instance_class (Callable[[], U]): A callable that creates an instance of the service.
        """
        if isinstance(interface, str):
            container[interface] = lambda c: instance_class()
        else:
            DependencyInjection._checkClass(instance_class, interface)
            instance = lambda c: instance_class()

            container[interface] = instance
            container[interface.__name__] = instance
                
    # TODO: Review implementation to verify if it is the same object in the same request
    @staticmethod
    def addScoped(interface: Type[T], instance_class: Type[U]) -> None:
        """
        Registers a service with a scoped lifetime.

        Scoped: Maintains the state of the service within a request. 
        Instances will only change when a new request is made.
        
        Args:
            interface (Type[T]): The interface type to register.
            instance_class (U): The class of the instance to be created.
        """
        DependencyInjection._checkClass(instance_class, interface)
        DependencyInjection.__register_request[interface] = instance_class            
        
    @staticmethod
    def addTransient(interface: Type[T], instance_class: Type[U]) -> None:
        """
        Registers a service with a transient lifetime.

        Transient: Temporary, as the literal translation suggests. A new instance of the object 
        will be created each time a request is made. While this can lead to higher memory and 
        resource usage, it can negatively impact performance. 
        Therefore, use it for lightweight services with little or no state.
        
        Args:
            interface (Type[T]): The interface type to register.
            instance_class (Type[U]): The class of the instance to be created.
        """
        if isinstance(interface, str):
            container.factories[interface] = lambda c: instance_class()
        else:
            DependencyInjection._checkClass(instance_class, interface)
            container.factories[interface] = lambda c: instance_class()
            container.factories[interface.__name__] = lambda c: instance_class()               
                