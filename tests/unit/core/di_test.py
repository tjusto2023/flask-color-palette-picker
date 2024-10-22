import pytest
from src.core.di import DependencyInjection
from src.core.config import Config

class TestDependencyInjection:       

    def test_add_singleton(self):
        # Given
        DependencyInjection.addSingleton(Config, Config)

        # Act
        resolved_instance1 = DependencyInjection.inject(Config) 
        resolved_instance2 = DependencyInjection.inject(Config) 

        # Assert
        
        assert isinstance(resolved_instance1, Config)
        assert isinstance(resolved_instance2, Config)
        assert resolved_instance1 is resolved_instance2

    def test_add_scoped(self):
        # Given
        DependencyInjection.addScoped(Config, Config)

        # Act        
        resolved_instance1 = DependencyInjection.inject(Config) 
        resolved_instance2 = DependencyInjection.inject(Config) 

        # Assert
        assert isinstance(resolved_instance1, Config)
        assert isinstance(resolved_instance2, Config)
        assert resolved_instance1 is not resolved_instance2

    @pytest.mark.skip(reason="Review implementation and skip test")
    def test_add_transient(self):
        # Act
        DependencyInjection.addTransient(Config, Config)

        # Assert
        resolved_instance1 = DependencyInjection.inject('Config') 
        resolved_instance2 = DependencyInjection.inject(Config)

        assert isinstance(resolved_instance1, Config)
        assert isinstance(resolved_instance2, Config)
        assert resolved_instance1 is not resolved_instance2