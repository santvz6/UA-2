class Coordenada{
    private:
        int x,y,z;
    public:
        Coordenada();
        Coordenada(int, int, int );// Sobrecarga del operador, es un método con constructor
        
        Coordenada(const Coordenada&); // Constructor de copia
        //usamos const y & para que no entre en un bucle de copias

        ~Coordenada();
        bool setX(int );
        bool setY(int );
        bool setZ(int );
        int getX() const;
        int getY() const;
        int getZ() const;
        void imprimir();
        
};