        subroutine simpson_malha(n,L,R,B_field_v)
        
        !calcula o campo magnetico numa malha que varre o plano xz
        
           integer kx,kz,p,q, n
           real*8  L, R, x, y, z, B(3), B_field_v(250,150,3)
           
!f2py intent(in) n, L, R, x, z
!f2py intent(out) B_field_v
           
           !dimensoes da malha
           p = 250
           q = 150
           
           B = 0.d0
           y = 0.d0
           do kx=1,p
              x = (kx-p/2)*5.d0*R/dble(p/2)
              do kz=1,q
                 z = (kz-q/3)*3.d0*L/dble(q)
                 
                 call simpson_ponto(n,L,R,x,y,z,B)
                 B_field_v(kx,kz,:) = B
                 
              end do
           end do
        
        end subroutine
        
!############################################################    
        subroutine simpson_malha_hor(n,L,R,B_field_h)
        
        !calcula o campo magnetico num plano paralelo a xy
        
           integer kx,ky,p,s, n
           real*8  L, R, x, y, z, B(3), B_field_h(250,250,3)
           
!f2py intent(in) n, L, R, x, z
!f2py intent(out) B_field_h
           
           !dimensoes da malha
           p = 250
           s = 250
           
           B = 0.d0
           z = L
           do kx=1,s
              x = (kx-p/2)*5.d0*R/dble(p/2)
              do ky=1,s
                 y = (ky-s/2)*5.d0*R/dble(s/2)
                 
                 call simpson_ponto(n,L,R,x,y,z,B)
                 B_field_h(kx,ky,:) = B
                 
              end do
           end do
        
        end subroutine
        
        
!#############################################################
        
        subroutine simpson_ponto(n,L,R,x,y,z,B)
        
        !calcula o campo magnetico num ponto do plano xz
        
          integer n, m, i, j
          real*8 L, R, B(3), Iv(3), pi, h, theta, dL,z0, dB(3), x,y,z
        
!f2py intent(in) n, L, R, x, z
!f2py intent(out) B   
          
          pi = datan2(0.d0,-1.d0)
          
          dL = L/(n-1)
          m = 100
          h = pi/m !(2*pi/m)/2
          
          B = 0.d0 !zera o campo
          Iv = 0.d0 !zera o vetor corrente
          
          !calcula o campo num po
          theta = h
          z0 = 0.d0
          !y = 0.d0
          do i=1,n
             do j=1,m
                !componentes da corrente na espira
                
                call deB(R,theta,z0, x,y,z, h, dB)
                !print*, dB
                B = B + dB
                
                
                theta = theta + 2*h
             end do
             z0 = z0 + dL !passa para a proxima espira
          end do
        
        end subroutine
        
        function a()
           real*8 a
           a=13.d0
        end function
        
        !contains
        
        subroutine deB(R,theta,z0, x,y,z, h, dB)
        
        !calcula a contribuicao de uma secao de espira na integral
        
           real*8 theta, dB(3), fl(3), fm(3), fr(3), z0, x,y,z,Iv(3)
           real*8 x0, y0, R, h, dR(3)
           
           Iv=0.d0
           
           !ponto do meio
           Iv(1) = -1.d0*sin(theta)   !corrente
           Iv(2) = cos(theta)         !corrente
           x0 = R*cos(theta)          !ponto
           y0 = R*sin(theta)          !ponto
           
           dR(1) = x - x0
           dR(2) = y - y0
           dR(3) = z - z0
           
           call cross(Iv,dR,fm) !calcula o prod. vetorial
           fm = fm/((x-x0)**2+(y0)**2+(z-z0)**2)**(3.0/2) !divide por dr^3/2
           
           !ponto da esquerda
           theta = theta - h
           Iv(1) = -1.d0*sin(theta)   !corrente
           Iv(2) = cos(theta)         !corrente
           x0 = R*cos(theta)          !ponto
           y0 = R*sin(theta)          !ponto
           
           dR(1) = x - x0
           dR(2) = y - y0
           dR(3) = z - z0
           
           call cross(Iv,dR,fl) !calcula o prod. vetorial
           fl = fl/((x-x0)**2+(y0)**2+(z-z0)**2)**(3.0/2) !divide por dr^3/2
           
           theta = theta + h !volta pro meio
           
           !ponto da direita
           theta = theta + h
           Iv(1) = -1.d0*sin(theta)   !corrente
           Iv(2) = cos(theta)         !corrente
           x0 = R*cos(theta)          !ponto
           y0 = R*sin(theta)          !ponto
           
           dR(1) = x - x0
           dR(2) = y - y0
           dR(3) = z - z0
           
           call cross(Iv,dR,fr) !calcula o prod. vetorial
           fr = fr/((x-x0)**2+(y-y0)**2+(z-z0)**2)**(3.0/2) !divide por dr^3/2
           
           theta = theta - h !volta pro meio
           
           !calcula a contribicao daquele pedacinho dada por simpson
           dB = (fl + 4*fm + fr)*h/3.d0
           !print*, dB
           
           
        end subroutine
        
        !calcula o produto vetorial de 2 vetores: a^b=c
        subroutine cross(a,b,c)
           real*8 a(3), b(3), c(3)
        
           c(1) = a(2)*b(3) - b(2)*a(3)
           c(2) = a(3)*b(1) - b(3)*a(1)
           c(3) = a(1)*b(2) - b(1)*a(2)
           
        end subroutine
        
        end
