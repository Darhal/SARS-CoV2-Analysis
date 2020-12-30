#include <iostream>
#include <thread>
#include <vector>
#include <utility>
#include <string>

template<typename T>
struct Matrix
{
    Matrix(uint64 N, uint64 M) : dimx(N), dimy(M)
    {
        _mat.resize(N*M);
    }

    T& operator()(uint64 x, uint64 y)
    {
        if (x >= dimx || y>= dimy)
            throw std::out_of_range("matrix indices out of range");
        return _mat[dimx*y + x];
    }

    const T& operator()(uint64 x, uint64 y) const
    {
        if (x >= dimx || y>= dimy)
            throw std::out_of_range("matrix indices out of range");
        return _mat[dimx*y + x];
    }

    std::vector<T> _mat;
    uint64 dimx, dimy;
};

struct Alignement
{
    const std::string seq1;
    const std::string seq2;
};

std::vector<Alignement> needleman_mt(
    const std::string& seq1, 
    const std::string& seq2, 
    uint64 match, uint64 mismatch, uint64 gap) 
{
    Matrix alignement_mat(seq1.size() + 1, seq2.size() + 1);
    Matrix mat_dir(seq1.size() + 1, seq2.size() + 1);

    uint64 len_seq1 = seq1.size();
    uint64 len_seq2 = seq2.size();

    for (uint64 i = 0; i < seq1.size() + 1; i++) {
        alignement_mat(0, i) = alignement_mat(0, i - 1) + gap
        mat_dir(0, i) = 1 << 1;
    }

    for (uint64 i = 0; i < seq2.size() + 1; i++) {
        alignement_mat(i, 0) = alignement_mat(i - 1, 0) + gap
        mat_dir(i, 0) = 1 << 1;
    }

    for (uint64 i = 1; i < len_seq2+1; i++){
        for (uint64 j =1 ; j < len_seq1+1; j++){
            uint64 left_val = alignement_mat(j, i - 1) + gap;
            uint64 up_val = alignement_mat(j - 1, i) + gap;
            alignement_mat(j, i) = max(max(left_val, up_val), diag_val);

            if diag_val == alignement_mat(j, i)
                mat_dir(j, i) | = 1
            if left_val == alignement_mat(j, i)
                mat_dir(j, i) |= (1 << 1)
            if up_val == alignement_mat(j, i)
                mat_dir(j, i) |= (1 << 2)
        }
    }


}

int main(int argc, char** argv)
{
    
    return 0;
}