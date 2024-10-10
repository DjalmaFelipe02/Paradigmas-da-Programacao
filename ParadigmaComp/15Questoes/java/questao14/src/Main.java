class Configuracao {
    private static Configuracao instanciaUnica = null;

    private String configuracao;

    // Construtor privado para evitar instanciação
    private Configuracao() {
        configuracao = "Configurações do Sistema";
    }

    // Método estático para retornar a única instância da classe
    public static Configuracao getInstancia() {
        if (instanciaUnica == null) {
            instanciaUnica = new Configuracao();
        }
        return instanciaUnica;
    }

    public String getConfiguracao() {
        return configuracao;
    }
}

public class Main {
    public static void main(String[] args) {
        Configuracao config1 = Configuracao.getInstancia();
        Configuracao config2 = Configuracao.getInstancia();

        System.out.println(config1.getConfiguracao());  // Exibe as configurações
        System.out.println(config1 == config2);  // Verifica se ambas as instâncias são iguais (devem ser)
    }
}
