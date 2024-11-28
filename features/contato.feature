Feature: Testar a página de contato do Instituto Joga Junto

  Scenario: Entrar na página de contato e inserir dados
    Given Entro na Página de contato do Instituto Joga Junto
    When Insiro meus dados
    Then Envio a mensagen "Teste - Oi Boa Noite!!"
