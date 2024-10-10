class SaldoInsuficienteException extends Exception {
    public SaldoInsuficienteException(String mensagem) {
        super(mensagem);
    }
}

class ContaBancaria {
    private double saldo;
    private String titular;

    ContaBancaria(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    public void depositar(double valor) {
        saldo += valor;
    }

    public void sacar(double valor) throws SaldoInsuficienteException {
        if (valor > saldo) {
            throw new SaldoInsuficienteException("Saldo insuficiente para realizar o saque.");
        }
        saldo -= valor;
    }

    public double getSaldo() {
        return saldo;
    }
}

public class Main {
    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria("João", 1000);

        try {
            conta.sacar(1500);  // Tentativa de saque que excede o saldo
        } catch (SaldoInsuficienteException e) {
            System.out.println(e.getMessage());
        }

        System.out.println("Saldo atual: " + conta.getSaldo());
    }
}
