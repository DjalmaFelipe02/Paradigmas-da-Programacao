interface Imprimivel {
    String imprimir();
}

class Relatorio implements Imprimivel {
    @Override
    public String imprimir() {
        return "Imprimindo Relatório...";
    }
}

class Contrato implements Imprimivel {
    @Override
    public String imprimir() {
        return "Imprimindo Contrato...";
    }
}

public class Main {
    public static void executarImpressao(Imprimivel imprimivel) {
        System.out.println(imprimivel.imprimir());
    }

    public static void main(String[] args) {
        Imprimivel relatorio = new Relatorio();
        Imprimivel contrato = new Contrato();

        executarImpressao(relatorio);
        executarImpressao(contrato);
    }
}
